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

  /* ─── LEAD FORMS (Buyer + Seller) — POST to /api/contact.php ─── */
  const API_ENDPOINT = '/api/contact.php';
  const MAILTO_FALLBACK = 'krish@goodmushroom.in,anmol@goodmushroom.in';

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

  function mailtoFallback(form) {
    const subjectEl = form.querySelector('[name="_subject"]');
    const subject = subjectEl ? subjectEl.value : 'New Enquiry — Good Mushroom';
    const data = new FormData(form);
    const lines = [];
    for (const [k, v] of data.entries()) {
      if (k.startsWith('_') || k === 'website' || !v) continue;
      const label = k.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
      lines.push(`${label}: ${v}`);
    }
    window.location.href = `mailto:${MAILTO_FALLBACK}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;
  }

  ['buyer-form', 'seller-form'].forEach(id => {
    document.querySelectorAll('#' + id).forEach(form => {
      form.querySelectorAll('[required]').forEach(field => {
        field.addEventListener('input', () => field.classList.remove('field-error'));
      });

      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!validateForm(form)) {
          const firstError = form.querySelector('.field-error');
          if (firstError) firstError.focus();
          return;
        }

        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn ? submitBtn.innerHTML : '';
        if (submitBtn) { submitBtn.disabled = true; submitBtn.innerHTML = 'Sending…'; }
        const successEl = form.querySelector('.success-msg');

        try {
          const res = await fetch(API_ENDPOINT, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } });
          const ct = res.headers.get('content-type') || '';
          const json = ct.includes('application/json') ? await res.json() : { ok: false, error: 'Bad response' };

          if (res.ok && json.ok) {
            if (successEl) {
              successEl.textContent = form.id === 'buyer-form'
                ? '✅ Thank you! We\'ve received your enquiry and will be in touch within 24 hours.'
                : '✅ Thank you for registering! Our sourcing team will contact you within 48 hours.';
              successEl.style.display = 'block';
            }
            form.reset();
            successEl?.scrollIntoView({ behavior: 'smooth', block: 'center' });
          } else {
            throw new Error(json.error || 'Submission failed');
          }
        } catch (err) {
          console.warn('Form submit failed, falling back to mailto:', err);
          if (successEl) {
            successEl.textContent = '⚠️ Connection issue — opening your email client as a backup. Please review and send.';
            successEl.style.display = 'block';
          }
          mailtoFallback(form);
        } finally {
          if (submitBtn) { submitBtn.disabled = false; submitBtn.innerHTML = originalText; }
        }
      });
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

  /* ─── CONTACT TAB FROM URL HASH (so #seller links open the seller form) ─── */
  function activateTabFromHash() {
    const hash = window.location.hash.replace('#','');
    if (!hash) return;
    const target = hash === 'seller' ? 'seller-panel'
                 : hash === 'buyer'  ? 'buyer-panel'
                 : null;
    if (!target) return;
    const btn = document.querySelector(`.tab-btn[data-tab="${target}"]`);
    if (btn) btn.click();
  }
  activateTabFromHash();
  window.addEventListener('hashchange', activateTabFromHash);

  /* ─── EXIT-INTENT MODAL ─── */
  const exitModal = document.getElementById('exitModal');
  if (exitModal) {
    const KEY = 'gm_exit_shown';
    const alreadyShown = sessionStorage.getItem(KEY);

    const openModal = () => {
      if (sessionStorage.getItem(KEY)) return;
      exitModal.classList.add('open');
      exitModal.setAttribute('aria-hidden','false');
      sessionStorage.setItem(KEY, '1');
    };
    const closeModal = () => {
      exitModal.classList.remove('open');
      exitModal.setAttribute('aria-hidden','true');
    };

    // Desktop: fire when cursor leaves the viewport top
    document.addEventListener('mouseleave', (e) => {
      if (e.clientY <= 0 && !alreadyShown) openModal();
    });

    // Mobile: fire after 25s of scrolling activity (exit intent doesn't exist on mobile)
    let scrolled = 0;
    const onScrollTrigger = () => { scrolled++; if (scrolled > 15 && window.scrollY > 1200) { openModal(); window.removeEventListener('scroll', onScrollTrigger); } };
    if (window.matchMedia('(max-width: 720px)').matches) {
      setTimeout(() => window.addEventListener('scroll', onScrollTrigger, { passive: true }), 25000);
    }

    // Close handlers
    exitModal.querySelector('.exit-modal-close').addEventListener('click', closeModal);
    exitModal.addEventListener('click', (e) => { if (e.target === exitModal) closeModal(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

    // Exit form posts to /api/contact.php (with mailto fallback on failure)
    const exitForm = document.getElementById('exitForm');
    if (exitForm) {
      exitForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const fd = new FormData(exitForm);
        if (!fd.get('form_type')) fd.set('form_type', 'spec_sheet');
        if (!fd.get('_subject')) fd.set('_subject', 'Export Spec Sheet Request — Good Mushroom');
        try {
          const res = await fetch('/api/contact.php', { method: 'POST', body: fd, headers: { 'Accept': 'application/json' } });
          const j = res.ok ? await res.json() : { ok: false };
          if (!j.ok) throw new Error('post failed');
        } catch {
          const subject = fd.get('_subject') || 'Website Enquiry — Good Mushroom';
          const lines = [];
          for (const [k,v] of fd.entries()) { if (!k.startsWith('_') && k !== 'website' && v) lines.push(`${k}: ${v}`); }
          window.location.href = `mailto:krish@goodmushroom.in,anmol@goodmushroom.in?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;
        }
        closeModal();
      });
    }
  }

});
