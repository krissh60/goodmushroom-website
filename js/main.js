/* ==========================================
   GOOD MUSHROOM — Main JavaScript
   ========================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ─── NAVBAR SCROLL BEHAVIOR ─── */
  const navbar = document.querySelector('.navbar');
  const navCta  = document.getElementById('navCta');
  if (navbar) {
    const onScroll = () => {
      const scrolled = window.scrollY > 80;
      navbar.classList.toggle('scrolled', scrolled);
      if (navCta) navCta.style.display = scrolled ? '' : 'none';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // run once on load
  }

  /* ─── MOBILE MENU ─── */
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileClose = document.querySelector('.mobile-close');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  }
  if (mobileClose && mobileMenu) {
    mobileClose.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      document.body.style.overflow = '';
    });
  }
  // Close on link click
  if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ─── ACTIVE NAV LINK ─── */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* ─── SCROLL REVEAL ─── */
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(el => {
        if (el.isIntersecting) {
          el.target.classList.add('visible');
          observer.unobserve(el.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => observer.observe(el));
  }

  /* ─── FAQ ACCORDION ─── */
  document.querySelectorAll('.faq-question').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.closest('.faq-item');
      const isOpen = item.classList.contains('open');
      // Close all
      document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
      // Open clicked if not already open
      if (!isOpen) item.classList.add('open');
    });
  });

  /* ─── CONTACT TABS ─── */
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      // Update buttons
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      // Update panels
      document.querySelectorAll('.form-panel').forEach(p => p.classList.remove('active'));
      const panel = document.getElementById(target);
      if (panel) panel.classList.add('active');
    });
  });

  /* ─── LEAD FORMS (Buyer + Seller) ─── */
  const MAILTO_TO = 'krish@goodmushroom.in,anmol@goodmushroom.in';

  function validateForm(form) {
    let isValid = true;
    form.querySelectorAll('[required]').forEach(field => {
      const val = field.value.trim();
      const empty = !val;
      const badEmail = field.type === 'email' && val && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
      const invalid = empty || badEmail;
      field.classList.toggle('field-error', invalid);
      if (invalid) isValid = false;
    });
    return isValid;
  }

  ['buyer-form', 'seller-form'].forEach(id => {
    const form = document.getElementById(id);
    if (!form) return;

    // Clear error state on input
    form.querySelectorAll('[required]').forEach(field => {
      field.addEventListener('input', () => field.classList.remove('field-error'));
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();

      if (!validateForm(form)) {
        const firstError = form.querySelector('.field-error');
        if (firstError) firstError.focus();
        return;
      }

      const subjectEl = form.querySelector('[name="_subject"]');
      const subject = subjectEl ? subjectEl.value : 'New Enquiry — Good Mushroom';

      const data = new FormData(form);
      const bodyLines = [];
      for (const [key, val] of data.entries()) {
        if (key.startsWith('_') || !val) continue;
        const label = key.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
        bodyLines.push(`${label}: ${val}`);
      }

      const mailtoUrl = `mailto:${MAILTO_TO}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(bodyLines.join('\n'))}`;

      const successEl = form.querySelector('.success-msg');
      if (successEl) {
        successEl.textContent = '✅ Your email client should open — please review and send the email to complete your enquiry.';
        successEl.style.display = 'block';
      }

      window.location.href = mailtoUrl;
    });
  });

  /* ─── PRODUCT FILTER (products page) ─── */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.product-card[data-category], .product-detail-card[data-category]');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.dataset.filter;
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      productCards.forEach(card => {
        if (cat === 'all' || card.dataset.category === cat) {
          card.style.display = '';
          setTimeout(() => card.style.opacity = '1', 10);
        } else {
          card.style.opacity = '0';
          setTimeout(() => card.style.display = 'none', 300);
        }
      });
    });
  });

  /* ─── ANIMATED COUNTER (hero stats) ─── */
  function animateCounter(el, target, suffix = '') {
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = Math.floor(current) + suffix;
    }, 16);
  }

  const statsSection = document.querySelector('.hero-stats');
  if (statsSection) {
    const counters = statsSection.querySelectorAll('.stat-num[data-target]');
    const statsObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          counters.forEach(counter => {
            const target = parseInt(counter.dataset.target);
            const suffix = counter.dataset.suffix || '';
            animateCounter(counter, target, suffix);
          });
          statsObserver.disconnect();
        }
      });
    }, { threshold: 0.5 });
    statsObserver.observe(statsSection);
  }

  /* ─── SMOOTH ANCHOR SCROLLING ─── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ─── BACK TO TOP ─── */
  const backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      backToTop.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ─── MARQUEE DUPLICATE for seamless loop ─── */
  const track = document.querySelector('.marquee-track');
  if (track) {
    const clone = track.innerHTML;
    track.innerHTML += clone;
  }

});
