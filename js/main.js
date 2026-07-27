/* ============================================================
   GOOD MUSHROOM — Site JS (design v4)
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Nav: scrolled state ---------- */
  const nav = document.querySelector('.nav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 8);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Active nav link ---------- */
  const here = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-links a, .mobile-menu-links a').forEach(a => {
    const href = (a.getAttribute('href') || '').toLowerCase();
    if (href === here || (here === '' && href === 'index.html')) a.classList.add('active');
  });

  /* ---------- Mobile menu ---------- */
  const menu = document.querySelector('.mobile-menu');
  const open = document.querySelector('.nav-hamburger');
  const close = document.querySelector('.mobile-menu-close');
  if (menu && open) {
    const setOpen = (v) => {
      menu.classList.toggle('open', v);
      document.body.style.overflow = v ? 'hidden' : '';
    };
    open.addEventListener('click', () => setOpen(true));
    if (close) close.addEventListener('click', () => setOpen(false));
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') setOpen(false); });
  }

  /* ---------- Scroll reveal (.reveal / .reveal-stagger) ---------- */
  const reveals = document.querySelectorAll('.reveal, .reveal-stagger');
  if (reveals.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });
    reveals.forEach(el => io.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('in'));
  }

  /* ---------- Product filters (products page) ---------- */
  const filters = document.querySelectorAll('.cat-filter');
  const cards = document.querySelectorAll('.cat-card[data-cat]');
  if (filters.length && cards.length) {
    filters.forEach(btn => {
      btn.addEventListener('click', () => {
        filters.forEach(f => f.classList.remove('active'));
        btn.classList.add('active');
        const f = btn.dataset.filter || 'all';
        cards.forEach(c => {
          const match = f === 'all' || (c.dataset.cat || '').split(/\s+/).includes(f);
          c.style.display = match ? '' : 'none';
        });
      });
    });
  }

  /* ---------- Contact form tabs ---------- */
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.form-panel').forEach(p => p.classList.remove('active'));
      const panel = document.getElementById(target);
      if (panel) panel.classList.add('active');
    });
  });

  /* ---------- Tab from hash ---------- */
  const fromHash = () => {
    const h = location.hash.replace('#','');
    const map = { buyer: 'buyer-panel', seller: 'seller-panel' };
    const target = map[h];
    if (!target) return;
    const btn = document.querySelector(`.tab-btn[data-tab="${target}"]`);
    if (btn) btn.click();
  };
  fromHash();
  window.addEventListener('hashchange', fromHash);

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq-question').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.closest('.faq-item');
      const open = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
      if (!open) item.classList.add('open');
    });
  });

  /* ---------- Lead forms — POST to /api/contact.php ---------- */
  const API_ENDPOINT = '/api/contact.php';

  /* ---------- Conversion attribution (no contact details sent to analytics) ---------- */
  const trackMainEvent = (name, data = {}) => {
    if (typeof gtag === 'function') gtag('event', name, data);
  };
  const currentPage = () => `${location.pathname}${location.search}`;
  const formContext = (form) => ({
    form_type: form.querySelector('[name="form_type"]')?.value || 'unknown',
    product: form.querySelector('[name="product"]')?.value || 'not_specified',
    source_page: form.querySelector('[name="source_page"]')?.value || currentPage(),
    page_path: location.pathname
  });
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link) return;
    const href = link.getAttribute('href') || '';
    const label = (link.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    if (/wa\.me\//i.test(href)) {
      trackMainEvent('whatsapp_click', { page_path: location.pathname, link_label: label || 'WhatsApp' });
    } else if (/request a quote/i.test(label) || /contact\.html#buyer/i.test(href)) {
      trackMainEvent('request_quote_click', { page_path: location.pathname, link_label: label || 'Request a Quote' });
    } else if (/apply as a supply partner|supplier application/i.test(label) || /contact\.html#seller/i.test(href)) {
      trackMainEvent('supplier_application_click', { page_path: location.pathname, link_label: label || 'Apply as a Supply Partner' });
    }
  });


  const validateForm = (form) => {
    let ok = true;
    form.querySelectorAll('[required]').forEach(field => {
      const val = (field.value || '').trim();
      const empty = !val;
      const badEmail = field.type === 'email' && val && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
      const invalid = empty || badEmail;
      field.classList.toggle('field-error', invalid);
      if (invalid) ok = false;
    });
    return ok;
  };

  const showFallbackError = (form) => {
    const successEl = form.querySelector('.success-msg');
    if (successEl) {
      successEl.textContent = '⚠ Something went wrong. Please try again, or message us on WhatsApp at +91 8219599053.';
      successEl.style.display = 'block';
      successEl.style.color = 'var(--ink-mid)';
    }
  };

  document.querySelectorAll('#buyer-form, #seller-form, #exitForm').forEach(form => {
    form.querySelectorAll('[required]').forEach(f => f.addEventListener('input', () => f.classList.remove('field-error')));

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!validateForm(form)) {
        form.querySelector('.field-error')?.focus();
        return;
      }
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalLabel = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) { submitBtn.disabled = true; submitBtn.innerHTML = 'Sending…'; }
      const successEl = form.querySelector('.success-msg');

      try {
        const res = await fetch(API_ENDPOINT, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } });
        const ct = res.headers.get('content-type') || '';
        const json = ct.includes('application/json') ? await res.json() : { ok: false, error: 'Bad response' };
        if (res.ok && json.ok) {
          const context = formContext(form);
          const eventName = context.form_type === 'buyer'
            ? 'buyer_form_submit'
            : context.form_type === 'seller'
              ? 'supplier_application_submit'
              : context.form_type === 'report'
                ? 'report_request_submit'
                : 'contact_form_submit';
          trackMainEvent(eventName, context);
          trackMainEvent('generate_lead', { lead_channel: context.form_type, product: context.product, page_path: context.page_path });
          if (successEl) {
            successEl.textContent = form.id === 'buyer-form'
              ? '✓ Thank you. We\'ve received your enquiry and will be in touch after review.'
                : form.id === 'seller-form'
                ? '✓ Thank you for registering. Our sourcing team will review the details and contact you if there is a route fit.'
                : '✓ Thank you — your request has been received.';
            successEl.style.display = 'block';
          }
          form.reset();
          successEl?.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
          throw new Error(json.error || 'Submission failed');
        }
      } catch (err) {
        console.warn('Form submit failed:', err);
        showFallbackError(form);
      } finally {
        if (submitBtn) { submitBtn.disabled = false; submitBtn.innerHTML = originalLabel; }
      }
    });
  });

  /* ---------- Smooth in-page scroll for hash links ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    const id = a.getAttribute('href');
    if (id.length < 2) return;
    const target = document.querySelector(id);
    if (!target) return;
    a.addEventListener('click', e => {
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
});
