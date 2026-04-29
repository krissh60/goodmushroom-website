<?php
/**
 * Good Mushroom — Contact form endpoint.
 * Handles buyer + seller + export spec-sheet enquiries from any page on the site.
 * Reads recipient + SMTP creds from /var/www/goodmushroom/api/.env
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Method not allowed']);
    exit;
}

/* ---- Load .env ---- */
function load_env(string $path): array {
    if (!is_readable($path)) return [];
    $env = [];
    foreach (file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
        $line = trim($line);
        if ($line === '' || $line[0] === '#') continue;
        if (!str_contains($line, '=')) continue;
        [$k, $v] = explode('=', $line, 2);
        $v = trim($v);
        if ((str_starts_with($v, '"') && str_ends_with($v, '"')) ||
            (str_starts_with($v, "'") && str_ends_with($v, "'"))) {
            $v = substr($v, 1, -1);
        }
        $env[trim($k)] = $v;
    }
    return $env;
}

$env = load_env(__DIR__ . '/.env');

$RECIPIENT_PRIMARY   = $env['RECIPIENT_PRIMARY']   ?? 'krish@goodmushroom.in';
$RECIPIENT_SECONDARY = $env['RECIPIENT_SECONDARY'] ?? 'anmol@goodmushroom.in';
$SMTP_HOST           = $env['SMTP_HOST']           ?? '';
$SMTP_PORT           = (int)($env['SMTP_PORT']     ?? 465);
$SMTP_USER           = $env['SMTP_USER']           ?? '';
$SMTP_PASS           = $env['SMTP_PASS']           ?? '';
$SMTP_FROM           = $env['SMTP_FROM']           ?? $SMTP_USER;
$SMTP_FROM_NAME      = $env['SMTP_FROM_NAME']      ?? 'Good Mushroom Website';
$RATE_LIMIT_PER_HOUR = (int)($env['RATE_LIMIT_PER_HOUR'] ?? 20);

/* ---- Honeypot (bots fill hidden 'website' field) ---- */
if (!empty($_POST['website'])) {
    echo json_encode(['ok' => true]); // pretend success to bot
    exit;
}

/* ---- Rate limit by IP, file-based ---- */
$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$ip = explode(',', $ip)[0];
$rate_dir = __DIR__ . '/logs';
@mkdir($rate_dir, 0750, true);
$rate_file = $rate_dir . '/rate_' . preg_replace('/[^a-zA-Z0-9._:-]/', '_', $ip) . '.log';
$now = time();
$hits = [];
if (is_readable($rate_file)) {
    $hits = array_filter(
        explode("\n", trim((string)file_get_contents($rate_file))),
        fn($t) => is_numeric($t) && (int)$t > $now - 3600
    );
}
if (count($hits) >= $RATE_LIMIT_PER_HOUR) {
    http_response_code(429);
    echo json_encode(['ok' => false, 'error' => 'Too many submissions. Please try again later or WhatsApp us directly.']);
    exit;
}
$hits[] = (string)$now;
@file_put_contents($rate_file, implode("\n", $hits));

/* ---- Validate ---- */
function clean(string $v, int $max = 1000): string {
    $v = trim(strip_tags($v));
    $v = preg_replace('/[\r\n]+/', ' ', $v);
    return mb_substr($v, 0, $max);
}

$form_type = $_POST['form_type'] ?? 'buyer';
$name      = clean($_POST['name']    ?? '', 120);
$email     = clean($_POST['email']   ?? '', 200);
$phone     = clean($_POST['phone']   ?? '', 60);
$message   = clean($_POST['message'] ?? '', 4000);

if ($form_type === 'seller') {
    if ($name === '' || $phone === '' || empty($_POST['state']) || empty($_POST['product'])) {
        http_response_code(400);
        echo json_encode(['ok' => false, 'error' => 'Missing required fields']);
        exit;
    }
} else {
    // buyer or spec_sheet
    if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode(['ok' => false, 'error' => 'Valid email required']);
        exit;
    }
    if ($form_type === 'buyer' && ($name === '' || empty($_POST['country']) || empty($_POST['product']))) {
        http_response_code(400);
        echo json_encode(['ok' => false, 'error' => 'Missing required fields']);
        exit;
    }
}

/* ---- Build email body ---- */
$subject_default = match ($form_type) {
    'seller'      => 'New Farmer/Seller Registration — Good Mushroom',
    'spec_sheet'  => 'Export Spec Sheet Request — Good Mushroom',
    default       => 'New Buyer Enquiry — Good Mushroom',
};
$subject = clean((string)($_POST['_subject'] ?? $subject_default), 200);

$lines = [];
$skip = ['_subject', 'website', 'form_type'];
foreach ($_POST as $k => $v) {
    if (in_array($k, $skip, true)) continue;
    if (is_array($v)) $v = implode(', ', $v);
    $v = clean((string)$v, 4000);
    if ($v === '') continue;
    $label = ucwords(str_replace('_', ' ', $k));
    $lines[] = sprintf('%s: %s', $label, $v);
}
$lines[] = '';
$lines[] = '---';
$lines[] = 'Submitted: ' . date('Y-m-d H:i:s T');
$lines[] = 'IP: ' . $ip;
$lines[] = 'User-Agent: ' . substr($_SERVER['HTTP_USER_AGENT'] ?? '', 0, 200);
$lines[] = 'Source: ' . substr($_SERVER['HTTP_REFERER'] ?? '(direct)', 0, 200);
$body_text = implode("\n", $lines);
$body_html = '<pre style="font-family:ui-monospace,monospace;font-size:13px;white-space:pre-wrap;">' .
             htmlspecialchars($body_text, ENT_QUOTES | ENT_HTML5, 'UTF-8') . '</pre>';

/* ---- Send via PHPMailer (SMTP) ---- */
require __DIR__ . '/lib/Exception.php';
require __DIR__ . '/lib/SMTP.php';
require __DIR__ . '/lib/PHPMailer.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception as PHPMailerException;

try {
    $mail = new PHPMailer(true);

    if ($SMTP_HOST !== '') {
        $mail->isSMTP();
        $mail->Host       = $SMTP_HOST;
        $mail->Port       = $SMTP_PORT;
        $mail->SMTPAuth   = true;
        $mail->Username   = $SMTP_USER;
        $mail->Password   = $SMTP_PASS;
        $mail->SMTPSecure = $SMTP_PORT === 465 ? PHPMailer::ENCRYPTION_SMTPS : PHPMailer::ENCRYPTION_STARTTLS;
        $mail->CharSet    = 'UTF-8';
    } else {
        // No SMTP configured — fall back to system mail() so dev/local still works.
        $mail->isMail();
    }

    $from_addr = $SMTP_FROM !== '' ? $SMTP_FROM : 'no-reply@goodmushroom.in';
    $mail->setFrom($from_addr, $SMTP_FROM_NAME);
    $mail->addAddress($RECIPIENT_PRIMARY);
    if ($RECIPIENT_SECONDARY !== '' && $RECIPIENT_SECONDARY !== $RECIPIENT_PRIMARY) {
        $mail->addAddress($RECIPIENT_SECONDARY);
    }
    if ($email !== '' && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $mail->addReplyTo($email, $name !== '' ? $name : $email);
    }

    $mail->Subject = $subject;
    $mail->isHTML(true);
    $mail->Body    = $body_html;
    $mail->AltBody = $body_text;

    $mail->send();

    @file_put_contents($rate_dir . '/sent.log',
        date('c') . "\t" . $form_type . "\t" . $email . "\t" . $name . "\t" . $ip . "\n",
        FILE_APPEND);

    echo json_encode(['ok' => true]);
} catch (PHPMailerException $e) {
    error_log('GoodMushroom mail send failed: ' . $mail->ErrorInfo);
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Email send failed. Please WhatsApp us at +91 6361 621 886.']);
} catch (\Throwable $e) {
    error_log('GoodMushroom mail unexpected: ' . $e->getMessage());
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Unexpected error. Please try again.']);
}
