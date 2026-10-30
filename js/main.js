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
      open.setAttribute('aria-expanded', String(v));
      if (!v && menu.contains(document.activeElement)) open.focus();
      menu.inert = !v;
      menu.setAttribute('aria-hidden', String(!v));
      document.body.style.overflow = v ? 'hidden' : '';
      if (v) close?.focus();
    };
    open.addEventListener('click', () => setOpen(true));
    if (close) close.addEventListener('click', () => setOpen(false));
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') setOpen(false);
      if (e.key !== 'Tab' || !menu.classList.contains('open')) return;
      const focusable = [...menu.querySelectorAll('a[href], button')];
      const first = focusable[0], last = focusable.at(-1);
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last?.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first?.focus(); }
    });
    setOpen(false);
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
  let applyingHash = false;
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      document.querySelectorAll('.tab-btn').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');
      document.querySelectorAll('.form-panel').forEach(p => p.classList.remove('active'));
      const panel = document.getElementById(target);
      if (panel) panel.classList.add('active');
      if (!applyingHash) history.replaceState(null, '', target === 'seller-panel' ? '#seller' : '#buyer');
    });
  });

  /* ---------- Tab from hash ---------- */
  const fromHash = () => {
    const h = location.hash.replace('#','');
    const map = { buyer: 'buyer-panel', specs: 'buyer-panel', seller: 'seller-panel' };
    const target = map[h];
    if (!target) return;
    const btn = document.querySelector(`.tab-btn[data-tab="${target}"]`);
    if (btn) {
      applyingHash = true;
      btn.click();
      applyingHash = false;
    }
  };
  fromHash();
  window.addEventListener('hashchange', fromHash);

  // Only known catalogue IDs can prefill a buyer enquiry.
  const productNames = {cordyceps:'Cordyceps Militaris', 'lions-mane':"Lion's Mane", oyster:'Oyster Mushrooms', ashwagandha:'Ashwagandha', reishi:'Reishi / Ganoderma', shiitake:'Shiitake', button:'Button & Specialty', 'extracts-dual':'Dual-Extract Powders', 'extracts-spore-oil':'Reishi Spore Oil', 'extracts-blends':'Mushroom Blends (custom)', tulsi:'Tulsi', 'shatavari-brahmi':'Shatavari / Brahmi'};
  const params = new URLSearchParams(location.search);
  const productId = params.get('product');
  const buyerForm = document.querySelector('#buyer-form');
  const prefillBuyer = () => {
   if (buyerForm && /\/contact(?:\.html)?$/.test(location.pathname) && Object.hasOwn(productNames, productId)) {
    const product = buyerForm.querySelector('select[name="product"]');
    if (product && Array.from(product.options).some(option => option.value === productNames[productId])) {
      product.value = productNames[productId];
      const source = buyerForm.querySelector('[name="source_page"]');
      if (source) source.value = `products/${productId}.html`;
    }
    const request = buyerForm.querySelector('[name="request_type"]');
    if (request && params.get('request') === 'specs') request.value = 'Product specifications';
   }
  };
  prefillBuyer();
  if (buyerForm && /\/contact(?:\.html)?$/.test(location.pathname) && Object.hasOwn(productNames, productId)) {
    document.querySelectorAll('a[data-track="quote"], a[data-track="specifications"]').forEach(link => {
      const target = new URL(link.href, location.href);
      if (target.origin !== location.origin || !/\/contact(?:\.html)?$/.test(target.pathname)) return;
      target.searchParams.set('product', productId);
      if (link.dataset.track === 'specifications') target.searchParams.set('request', 'specs');
      else target.searchParams.delete('request');
      target.hash = link.dataset.track === 'specifications' ? 'specs' : 'buyer';
      link.href = target.pathname + target.search + target.hash;
      link.dataset.product = productId;
    });
  }

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
  const currentPage = () => location.pathname;
  const formContext = (form) => {
    const type = form.querySelector('[name="form_type"]')?.value;
    const selected = form.querySelector('[name="product"]')?.value;
    const selectedId = Object.keys(productNames).find(id => productNames[id] === selected);
    const source = form.querySelector('[name="source_page"]')?.value;
    const sourceId = Object.keys(productNames).find(id => source === `products/${id}.html`);
    return {
      form_type: ['buyer', 'seller', 'report'].includes(type) ? type : 'other',
      product_id: selectedId || (form.querySelector('[name="product"]')?.type === 'hidden' && sourceId) || 'unspecified',
      request_kind: form.querySelector('[name="request_type"]')?.value === 'Product specifications' ? 'specifications' : 'enquiry',
      source_page: sourceId ? `/products/${sourceId}.html` : currentPage(),
      page_path: location.pathname
    };
  };
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link) return;
    const events = {ingredient:'ingredient_select', whatsapp:'whatsapp_click', specifications:'specification_request_click', quote:'request_quote_click', supplier:'supplier_application_click'};
    const name = events[link.dataset.track];
    if (name) trackMainEvent(name, {page_path: location.pathname, product_id: Object.hasOwn(productNames, link.dataset.product) ? link.dataset.product : 'unspecified'});
  });


  const validateForm = (form) => {
    let ok = true;
    form.querySelectorAll('[required], input[type="email"]').forEach(field => {
      const val = (field.value || '').trim();
      const empty = field.required && !val;
      const badEmail = field.type === 'email' && val && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
      const invalid = empty || badEmail;
      field.classList.toggle('field-error', invalid);
      field.setAttribute('aria-invalid', String(invalid));
      if (invalid) ok = false;
    });
    return ok;
  };

  const showFallbackError = (form, message) => {
    const successEl = form.querySelector('.success-msg');
    if (successEl) {
      successEl.textContent = message || 'Something went wrong. Please try again, or message us on WhatsApp at +91 8219599053.';
      successEl.style.display = 'block';
      successEl.style.color = 'var(--ink-mid)';
    }
  };

  document.querySelectorAll('#buyer-form, #seller-form, #exitForm').forEach(form => {
    let sending = false;
    form.addEventListener('focusin', () => trackMainEvent('enquiry_start', formContext(form)), {once:true});
    form.querySelectorAll('[required], input[type="email"]').forEach(f => f.addEventListener('input', () => {
      f.classList.remove('field-error');
      f.removeAttribute('aria-invalid');
    }));

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (sending) return;
      if (!validateForm(form)) {
        trackMainEvent('enquiry_error', {...formContext(form), error_type:'validation'});
        form.querySelector('.field-error')?.focus();
        return;
      }
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalLabel = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) { submitBtn.disabled = true; submitBtn.innerHTML = 'Sending…'; }
      const successEl = form.querySelector('.success-msg');
      sending = true;
      if (successEl) successEl.style.display = 'none';
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 20000);

      try {
        const res = await fetch(API_ENDPOINT, { method: 'POST', body: new FormData(form), signal:controller.signal, headers: { 'Accept': 'application/json' } });
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
          // The honeypot returns a generic success, but no mail was sent.
          if (json.mail_accepted === true) {
            trackMainEvent(eventName, context);
            trackMainEvent('generate_lead', { ...context, lead_channel: context.form_type });
          }
          if (successEl) {
            successEl.textContent = form.id === 'buyer-form'
              ? '✓ Thank you. We\'ve received your enquiry and will be in touch after review.'
                : form.id === 'seller-form'
                ? '✓ Thank you for registering. Our sourcing team will review the details and contact you if there is a route fit.'
                : '✓ Thank you — your request has been received.';
            successEl.style.display = 'block';
            successEl.style.color = '';
          }
          form.reset();
          if (form === buyerForm) prefillBuyer();
          successEl?.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
          throw new Error(json.error || 'Submission failed');
        }
      } catch (err) {
        trackMainEvent('enquiry_error', {...formContext(form), error_type:err.name === 'AbortError' ? 'timeout' : 'delivery'});
        showFallbackError(form, err.message === 'Too many submissions. Please try again later or WhatsApp us directly.' ? err.message : undefined);
      } finally {
        clearTimeout(timeout);
        sending = false;
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
