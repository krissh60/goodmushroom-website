/* Production-only Google Analytics. Local previews never initialize collection. */
(() => {
  if (!['goodmushroom.in', 'www.goodmushroom.in'].includes(location.hostname)) return;
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  const url = new URL(location.href);
  // Contact details must never be added to a page URL. Drop common accidental keys.
  for (const key of [...url.searchParams.keys()]) {
    if (/email|phone|name|message|address|company/i.test(key)) url.searchParams.delete(key);
  }
  url.hash = '';
  gtag('js', new Date());
  gtag('config', 'G-3JPKHJHFQM', {page_location:url.href});
  const tag = document.createElement('script');
  tag.async = true;
  tag.src = 'https://www.googletagmanager.com/gtag/js?id=G-3JPKHJHFQM';
  document.head.appendChild(tag);
})();
