(() => {
  'use strict';
  const $ = s => document.querySelector(s);
  const $$ = s => Array.from(document.querySelectorAll(s));
  let language = 'en';
  let topic = 'all';
  const articles = $$('.publication');
  const search = $('#paper-search');
  const year = $('#paper-year');
  const t = (en, zh) => language === 'zh' ? zh : en;
  function filterPapers() {
    if (!search) return;
    const query = search.value.trim().toLowerCase();
    let count = 0;
    articles.forEach(article => {
      const matches = (topic === 'all' || article.dataset.topic === topic) &&
        (!year.value || article.dataset.year === year.value) &&
        (!query || article.textContent.toLowerCase().includes(query));
      article.hidden = !matches;
      if (matches) count++;
    });
    $('#results-status').textContent = t(`${count} ${count === 1 ? 'publication' : 'publications'}`,`显示 ${count} 条成果`);
    $('#no-results').hidden = count > 0;
    $$('.filter').forEach(b => b.setAttribute('aria-pressed',String(b.dataset.topic === topic)));
  }
  function setLanguage(lang) {
    language = lang === 'zh' ? 'zh' : 'en';
    document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    $$('[data-en][data-zh]').forEach(el => { el.textContent = el.dataset[language]; });
    $$('[data-placeholder-en]').forEach(el => { el.placeholder = el.dataset[language === 'zh' ? 'placeholderZh' : 'placeholderEn']; });
    $$('.language button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === language)));
    $('#menu-toggle').setAttribute('aria-label', t('Toggle navigation','展开或收起导航'));
    document.title = t(`${document.body.dataset.titleEn} | Xiaodong Yang`, `${document.body.dataset.titleZh} | 杨晓东`);
    try { localStorage.setItem('xy-language', language); } catch (_) { /* Storage may be unavailable in private browsing. */ }
    filterPapers();
  }
  $$('.language button').forEach(b => b.addEventListener('click', () => setLanguage(b.dataset.lang)));
  $$('.filter').forEach(b => b.addEventListener('click', () => { topic=b.dataset.topic; filterPapers(); }));
  if (search) {
  search.addEventListener('input', () => { filterPapers(); });
  search.addEventListener('keydown', e => { if(e.key==='Escape'){ search.value=''; filterPapers(); } });
  year.addEventListener('change', () => { filterPapers(); });
  $('#reset-filters').addEventListener('click', () => { topic='all'; search.value=''; year.value=''; filterPapers(); search.focus(); });
  }
  const menu=$('#menu-toggle'), nav=$('#main-nav');
  menu.addEventListener('click', () => { const expanded=menu.getAttribute('aria-expanded')!=='true'; menu.setAttribute('aria-expanded',String(expanded)); nav.classList.toggle('open',expanded); });
  $$('#main-nav a').forEach(a => a.addEventListener('click', () => { nav.classList.remove('open'); menu.setAttribute('aria-expanded','false'); }));
  document.addEventListener('keydown', e => { if(e.key==='Escape' && nav.classList.contains('open')){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.focus();} });
  let saved='en'; try { saved=localStorage.getItem('xy-language') || 'en'; } catch (_) {}
  setLanguage(saved);
})();
