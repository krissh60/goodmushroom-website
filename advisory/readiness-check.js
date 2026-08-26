/* Good Mushroom Advisory — browser-only project-readiness screening. */
(function(){
  var root = document.querySelector('[data-readiness-tool]');
  if(!root) return;
  var form = document.getElementById('readiness-check-form');
  var steps = Array.prototype.slice.call(root.querySelectorAll('.readiness-step'));
  var nextButton = root.querySelector('[data-next]');
  var prevButton = root.querySelector('[data-prev]');
  var submitButton = root.querySelector('[data-submit]');
  var error = root.querySelector('[data-form-error]');
  var result = root.querySelector('[data-result]');
  var progressLabel = root.querySelector('[data-progress-label]');
  var progressBar = root.querySelector('[data-progress-bar]');
  var currentStep = 0;
  var started = false;

  var labels = {
    intent: {'new-project':'new project planning','existing-farm':'existing-farm review','funding':'funding or DPR preparation','buyer-route':'buyer-route planning','research':'early research'},
    species: {button:'button mushroom',oyster:'oyster mushroom',milky:'milky mushroom','cordyceps-militaris':'Cordyceps militaris',other:'another species','not-sure':'an undecided species'},
    space: {'under-1000':'under 1,000 sq ft','1000-5000':'1,000–5,000 sq ft','5000-15000':'5,000–15,000 sq ft','over-15000':'more than 15,000 sq ft','not-decided':'an undecided space'},
    budget: {'under-5':'below ₹5 lakh','5-25':'₹5–25 lakh','25-100':'₹25 lakh–₹1 crore','over-100':'above ₹1 crore','not-decided':'an undecided budget'},
    timeline: {now:'the next 30 days',quarter:'the next 1–3 months',later:'the next 3–12 months',exploring:'an exploratory timeline'},
    experience: {none:'no commercial experience',small:'small or informal experience',commercial:'commercial farm experience',adjacent:'adjacent food or agriculture experience'},
    buyerRoute: {local:'local retail, restaurants or institutions',wholesale:'wholesale or distribution',processor:'a processor or ingredient buyer',direct:'direct-to-consumer',other:'another route'}
  };

  function track(name, params){
    if(typeof window.gtag === 'function') window.gtag('event', name, params || {});
  }
  function value(name){
    var field = form.elements[name];
    return field ? field.value : '';
  }
  function checkedUtilities(){
    return Array.prototype.slice.call(form.querySelectorAll('input[name="utility"]:checked')).map(function(input){return input.value;});
  }
  function showStep(index){
    currentStep = index;
    steps.forEach(function(step, i){
      var active = i === index;
      step.hidden = !active;
      step.classList.toggle('is-active', active);
    });
    prevButton.hidden = index === 0;
    nextButton.hidden = index === steps.length - 1;
    submitButton.hidden = index !== steps.length - 1;
    progressLabel.textContent = 'Step ' + (index + 1) + ' of ' + steps.length;
    progressBar.style.width = (((index + 1) / steps.length) * 100) + '%';
    error.hidden = true;
    if(!started){ started = true; track('readiness_check_start'); }
  }
  function validCurrentStep(){
    var required = steps[currentStep].querySelectorAll('[required]');
    var okay = true;
    Array.prototype.forEach.call(required, function(field){
      var fieldOkay = field.type === 'radio' ? form.querySelector('input[name="' + field.name + '"]:checked') : Boolean(field.value);
      field.closest('.readiness-field, .readiness-options')?.classList.toggle('has-error', !fieldOkay);
      if(!fieldOkay) okay = false;
    });
    if(!okay){ error.hidden = false; return false; }
    track('readiness_check_step_complete', {step: currentStep + 1});
    return true;
  }
  function textFor(group, raw){ return (labels[group] && labels[group][raw]) || raw || 'not specified'; }
  function unique(list){ return list.filter(function(item, index){ return item && list.indexOf(item) === index; }); }
  function buildResult(){
    var intent = value('intent'), species = value('species'), space = value('space'), budget = value('budget'), timeline = value('timeline'), experience = value('experience'), buyerRoute = value('buyerRoute'), utilities = checkedUtilities();
    var signals = [], gaps = [], resultType, title, summary, next;
    if(intent) signals.push('Your immediate decision is ' + textFor('intent', intent) + '.');
    if(species && species !== 'not-sure') signals.push('You have a direction for ' + textFor('species', species) + '.'); else gaps.push('Choose and compare a species or product direction before committing to a facility design.');
    if(space && space !== 'not-decided') signals.push('A project-space range is identified: ' + textFor('space', space) + '.'); else gaps.push('Confirm the usable space, layout constraints and site access.');
    if(utilities.indexOf('water') >= 0 && utilities.indexOf('power') >= 0) signals.push('Water and power are marked as available at the likely site.'); else gaps.push('Validate reliable water and power; access and site conditions can change the design.');
    if(budget && budget !== 'not-decided') signals.push('You have selected ' + textFor('budget', budget) + ' as a working budget band.'); else gaps.push('Set a working budget range and separate available capital from borrowing assumptions.');
    if(timeline === 'now' || timeline === 'quarter') signals.push('The decision has a near-term window: ' + textFor('timeline', timeline) + '.'); else gaps.push('Turn the timeline into a dated decision window and list what must be true before spending.');
    if(buyerRoute) signals.push('A possible route to market is ' + textFor('buyerRoute', buyerRoute) + '.'); else gaps.push('Name the first credible buyer route and what evidence it would require.');
    if(experience === 'commercial' || experience === 'adjacent') signals.push('Relevant operating experience is available to build on.'); else if(experience === 'none' || experience === 'small') gaps.push('Plan an operator, training and day-to-day execution support before scaling.');

    var strongSignals = (species && species !== 'not-sure' ? 1 : 0) + (space && space !== 'not-decided' ? 1 : 0) + (utilities.indexOf('water') >= 0 && utilities.indexOf('power') >= 0 ? 1 : 0) + (budget && budget !== 'not-decided' ? 1 : 0) + (timeline === 'now' || timeline === 'quarter' ? 1 : 0) + (buyerRoute ? 1 : 0);
    if(intent === 'research' || timeline === 'exploring' || strongSignals <= 2){
      resultType = 'early-stage'; title = 'Start with validation before a large commitment.'; summary = 'Your answers are useful for framing the question, but too many project variables are still open for a responsible feasibility conversation.'; next = 'Use the gaps below to prepare a short project brief. A human review can help you decide which unknown to validate first.';
    } else if(strongSignals >= 5 && gaps.length <= 2){
      resultType = 'promising-fit'; title = 'Promising fit for a qualification discussion.'; summary = 'You have several of the early signals needed to choose a focused next step. The result still needs site, technical, market and financial validation.'; next = 'Bring your selected species, site range, utility status, budget band and route-to-market question to a qualification call.';
    } else {
      resultType = 'needs-validation'; title = 'Needs validation before you commit.'; summary = 'There is enough direction to continue, but one or more operating, commercial or commitment inputs should be checked before a detailed plan is prepared.'; next = 'Work through the missing-input list, then request a focused review if you want help prioritising the next evidence.';
    }
    return {type:resultType,title:title,summary:summary,next:next,signals:unique(signals),gaps:unique(gaps),species:species,intent:intent};
  }
  function renderList(target, items, fallback){
    target.innerHTML = '';
    (items.length ? items : [fallback]).forEach(function(item){ var li = document.createElement('li'); li.textContent = item; target.appendChild(li); });
  }
  function showResult(){
    if(!validCurrentStep()) return;
    var data = buildResult();
    form.hidden = true;
    root.querySelector('.readiness-progress').hidden = true;
    result.hidden = false;
    result.dataset.resultType = data.type;
    root.querySelector('[data-result-title]').textContent = data.title;
    root.querySelector('[data-result-summary]').textContent = data.summary;
    root.querySelector('[data-result-next]').textContent = data.next;
    root.querySelector('[data-result-eyebrow]').textContent = data.type === 'promising-fit' ? 'Promising fit' : data.type === 'needs-validation' ? 'Needs validation' : 'Early-stage screen';
    renderList(root.querySelector('[data-result-signals]'), data.signals, 'No strong readiness signal was selected yet.');
    renderList(root.querySelector('[data-result-gaps]'), data.gaps, 'No additional gap was identified by this short screen; a full review is still required.');
    track('readiness_check_result', {result_type:data.type, species:data.species || 'not-specified', intent:data.intent || 'not-specified'});
    result.scrollIntoView({behavior:'smooth', block:'start'});
  }
  function summaryText(){
    var data = buildResult();
    return 'Good Mushroom Advisory project-readiness screen\nResult: ' + data.title + '\nSummary: ' + data.summary + '\nSignals:\n- ' + data.signals.join('\n- ') + '\nValidate next:\n- ' + data.gaps.join('\n- ') + '\nSuggested next step: ' + data.next;
  }
  nextButton.addEventListener('click', function(){ if(validCurrentStep()) showStep(currentStep + 1); });
  prevButton.addEventListener('click', function(){ showStep(Math.max(0, currentStep - 1)); });
  form.addEventListener('submit', function(event){ event.preventDefault(); showResult(); });
  root.querySelector('[data-copy]').addEventListener('click', function(){
    var button = this, text = summaryText();
    if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(text).then(function(){button.textContent = 'Summary copied'; track('readiness_check_copy');}); }
    else { button.textContent = 'Select the summary manually'; track('readiness_check_copy_unavailable'); }
  });
  root.querySelector('[data-reset]').addEventListener('click', function(){
    form.reset(); form.hidden = false; result.hidden = true; root.querySelector('.readiness-progress').hidden = false; result.removeAttribute('data-result-type'); showStep(0); window.scrollTo({top:root.offsetTop - 24, behavior:'smooth'});
  });
  root.querySelector('[data-result-cta]').addEventListener('click', function(){ track('readiness_check_cta_click', {result_type:result.dataset.resultType || 'unknown'}); });
  showStep(0);
}());
