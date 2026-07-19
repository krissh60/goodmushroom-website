/* Shared Good Mushroom navigation/footer for Advisory pages. */
(function(){
  var nav = [
    '<nav class="nav" aria-label="Advisory">',
      '<div class="nav-inner">',
        '<a href="/" class="nav-logo" aria-label="Good Mushroom Advisory — home">',
          '<span class="nav-logo-mark" aria-hidden="true"></span><span>Good Mushroom</span>',
          '<img src="/images/logo-nav.png" alt="Good Mushroom" class="brand-img" width="343" height="96">',
        '</a>',
        '<ul class="nav-links" role="list">',
          '<li><a href="/#services">Services</a></li>',
          '<li><a href="/services/mushroom-farm-dpr-india.html">DPR &amp; Project Plans</a></li>',
          '<li><a href="https://goodmushroom.in/reports.html">Reports</a></li>',
          '<li><a href="/resources/">Resources</a></li>',
          '<li><a href="/#faq">FAQ</a></li>',
          '<li><a href="https://goodmushroom.in/">Trading &amp; Supply</a></li>',
        '</ul>',
        '<div class="nav-cta">',
          '<a href="/#request" class="btn btn-primary btn-sm">Request advisory</a>',
          '<button class="nav-hamburger" aria-label="Open menu" aria-expanded="false">',
            '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
          '</button>',
        '</div>',
      '</div>',
    '</nav>',
    '<div class="mobile-menu" role="dialog" aria-label="Advisory menu" aria-modal="true">',
      '<div class="mobile-menu-top">',
        '<a href="/" class="nav-logo" aria-label="Good Mushroom Advisory — home">',
          '<span class="nav-logo-mark" aria-hidden="true"></span><span>Good Mushroom</span>',
          '<img src="/images/logo-nav.png" alt="Good Mushroom" class="brand-img" width="343" height="96">',
        '</a>',
        '<button class="mobile-menu-close" aria-label="Close menu">×</button>',
      '</div>',
      '<nav class="mobile-menu-links" aria-label="Advisory navigation">',
        '<a href="/#services">Services <span class="arr">→</span></a>',
        '<a href="/services/mushroom-farm-dpr-india.html">DPR &amp; Project Plans <span class="arr">→</span></a>',
        '<a href="https://goodmushroom.in/reports.html">Reports <span class="arr">→</span></a>',
        '<a href="/resources/">Resources <span class="arr">→</span></a>',
        '<a href="/#faq">FAQ <span class="arr">→</span></a>',
        '<a href="https://goodmushroom.in/">Trading &amp; Supply <span class="arr">→</span></a>',
      '</nav>',
      '<div class="mobile-menu-foot">',
        '<a href="/#request" class="btn btn-primary btn-lg">Request advisory →</a>',
        '<a href="https://wa.me/918219599053" class="btn btn-outline btn-lg">Chat on WhatsApp</a>',
      '</div>',
    '</div>'
  ].join('');

  var footer = [
    '<footer class="foot">',
      '<div class="wrap">',
        '<div class="foot-grid">',
          '<div class="foot-brand">',
            '<img src="/images/logo-white.png" alt="Good Mushroom" class="brand-img" width="802" height="225">',
            '<h3>Good <em>Mushroom</em></h3>',
            '<p>Commercial mushroom reports, DPRs and project-planning support for founders making careful business decisions.</p>',
          '</div>',
          '<div class="foot-col">',
            '<h5>Advisory</h5>',
            '<ul>',
              '<li><a href="/#services">Services</a></li>',
              '<li><a href="https://goodmushroom.in/reports.html">Commercial reports</a></li>',
              '<li><a href="/services/mushroom-farm-dpr-india.html">DPR &amp; project plans</a></li>',
              '<li><a href="/resources/">Resources</a></li>',
              '<li><a href="/#faq">FAQ</a></li>',
            '</ul>',
          '</div>',
          '<div class="foot-col">',
            '<h5>Good Mushroom</h5>',
            '<ul>',
              '<li><a href="https://goodmushroom.in/">Trading &amp; supply</a></li>',
              '<li><a href="https://goodmushroom.in/products.html">Product catalogue</a></li>',
              '<li><a href="https://goodmushroom.in/buyers.html">For buyers</a></li>',
              '<li><a href="https://goodmushroom.in/contact.html">Contact</a></li>',
              '<li><a href="https://goodmushroom.in/privacy.html">Privacy</a></li>',
            '</ul>',
          '</div>',
          '<div class="foot-col">',
            '<h5>Contact</h5>',
            '<div class="foot-contact">',
              '<a href="mailto:info@goodmushroom.in">info@goodmushroom.in</a>',
              '<a href="https://wa.me/918219599053">+91 82195 99053</a>',
              '<span>Himachal Pradesh, India</span>',
              '<span>Mon–Sat · 10am–6pm IST</span>',
            '</div>',
          '</div>',
        '</div>',
        '<div class="foot-bottom"><span>© 2026 Good Mushroom PVT LTD · All rights reserved</span><span>Made with care in India</span></div>',
      '</div>',
    '</footer>'
  ].join('');

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){window.dataLayer.push(arguments);};
  window.gtag('js', new Date());
  window.gtag('config', 'G-3JPKHJHFQM');
  var analyticsScript = document.createElement('script');
  analyticsScript.async = true;
  analyticsScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-3JPKHJHFQM';
  document.head.appendChild(analyticsScript);

  document.body.insertAdjacentHTML('afterbegin', nav);
  document.body.insertAdjacentHTML('beforeend', footer);

  var open = document.querySelector('.nav-hamburger');
  var menu = document.querySelector('.mobile-menu');
  var close = document.querySelector('.mobile-menu-close');
  function closeMenu(){
    if(!menu) return;
    menu.classList.remove('open');
    document.body.style.overflow = '';
    if(open) open.setAttribute('aria-expanded', 'false');
  }
  if(open && menu){
    open.addEventListener('click', function(){
      menu.classList.add('open');
      document.body.style.overflow = 'hidden';
      open.setAttribute('aria-expanded', 'true');
    });
    if(close) close.addEventListener('click', closeMenu);
    menu.querySelectorAll('a').forEach(function(link){ link.addEventListener('click', closeMenu); });
  }
}());
