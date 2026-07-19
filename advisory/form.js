(function(){
  var form=document.getElementById('advisory-form'); if(!form)return;
  var select=document.getElementById('service_wanted');
  var success=form.querySelector('.adv-success');
  var error=form.querySelector('.adv-error');
  var params=new URLSearchParams(window.location.search);
  var preset=params.get('service');
  var started=false;

  /* Never send contact details or free text to analytics. */
  function track(name, data){
    if(typeof gtag==='function') gtag('event',name,data||{});
  }
  function setHidden(name,value){
    var field=form.querySelector('[name="'+name+'"]');
    if(!field){
      field=document.createElement('input');
      field.type='hidden';
      field.name=name;
      form.appendChild(field);
    }
    field.value=value||'';
  }
  function serviceValue(){ return select&&select.value ? select.value : 'not_selected'; }
  function syncAttribution(){
    setHidden('source_page',window.location.origin+window.location.pathname);
    ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(function(name){
      setHidden(name,params.get(name)||'');
    });
  }
  function syncSubject(){
    var field=form.querySelector('[name="_subject"]');
    if(field) field.value='New Advisory Enquiry — '+serviceValue();
  }
  function choose(value){
    var matched=false;
    Array.prototype.forEach.call(select.options,function(option){
      if(option.text.indexOf(value)===0){option.selected=true;matched=true;}
    });
    return matched;
  }
  function markStarted(){
    if(started)return;
    started=true;
    track('advisory_form_start',{service:serviceValue(),page_path:window.location.pathname});
  }

  syncAttribution();
  if(preset) choose(preset);

  document.querySelectorAll('[data-service]').forEach(function(link){
    link.addEventListener('click',function(){
      var service=link.getAttribute('data-service');
      choose(service);
      track('advisory_cta_click',{service:service,page_path:window.location.pathname,placement:link.getAttribute('data-placement')||'service_card'});
    });
  });
  select.addEventListener('change',function(){
    markStarted();
    if(select.value) track('advisory_service_select',{service:select.value,page_path:window.location.pathname});
  });
  form.addEventListener('focusin',markStarted);

  form.addEventListener('submit',function(event){
    event.preventDefault();
    success.style.display='none';
    error.style.display='none';
    var valid=true;
    form.querySelectorAll('[required]').forEach(function(field){
      var missing=field.type==='checkbox'?!field.checked:!String(field.value||'').trim();
      field.setAttribute('aria-invalid',missing?'true':'false');
      if(missing)valid=false;
    });
    if(!valid){
      error.textContent='Please complete the required fields before sending your request.';
      error.style.display='block';
      form.querySelector('[aria-invalid="true"]').focus();
      return;
    }

    markStarted();
    syncAttribution();
    syncSubject();
    var service=serviceValue();
    track('advisory_request_submit',{service:service,page_path:window.location.pathname});

    var button=form.querySelector('button[type="submit"]');
    var label=button.innerHTML;
    button.disabled=true;
    button.innerHTML='Sending…';

    fetch(form.action,{method:'POST',body:new FormData(form),headers:{Accept:'application/json'}})
      .then(function(response){if(!response.ok)throw new Error('Request failed');return response.json();})
      .then(function(data){
        if(!data.ok)throw new Error('Request failed');
        track('generate_lead',{lead_channel:'advisory_form',service:service,page_path:window.location.pathname});
        success.textContent='Thanks—your request is with us. We will review the service fit and send the appropriate payment and intake instructions manually. DPR and custom work begin with the paid qualification call.';
        success.style.display='block';
        form.reset();
        syncAttribution();
        success.scrollIntoView({behavior:'smooth',block:'center'});
      })
      .catch(function(){
        track('advisory_request_error',{service:service,page_path:window.location.pathname});
        error.textContent='We could not send the form. Please email info@goodmushroom.in with the advisory service you need.';
        error.style.display='block';
      })
      .finally(function(){button.disabled=false;button.innerHTML=label;});
  });
}());