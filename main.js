// Piccole interazioni: header al passaggio, comparsa delle sezioni, galleria.
document.documentElement.classList.add('js');

const header = document.querySelector('.site-header');
const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 8);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

const items = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  items.forEach((el) => io.observe(el));
} else {
  items.forEach((el) => el.classList.add('in'));
}

const gallery = document.querySelector('.gallery');
document.querySelectorAll('[data-gallery]').forEach((btn) => {
  btn.addEventListener('click', () => {
    const dir = btn.dataset.gallery === 'next' ? 1 : -1;
    gallery.scrollBy({ left: dir * 260, behavior: 'smooth' });
  });
});

// Selettore lingua: ricorda la scelta (unico dato salvato nel browser, vedi cookie policy).
document.querySelectorAll('.lang a[data-lang]').forEach((a) => {
  a.addEventListener('click', () => {
    try { localStorage.setItem('oywa-lang', a.dataset.lang); } catch (e) { /* storage non disponibile */ }
  });
});
document.addEventListener('click', (e) => {
  document.querySelectorAll('.lang[open]').forEach((d) => { if (!d.contains(e.target)) d.removeAttribute('open'); });
});

// Pulsanti iPhone/Android: prima di aprire la mail chiede il nome (obbligatorio).
// Il link mailto dei pulsanti termina con "Nome: " nel testo: qui ci aggiungiamo il nome.
// Da telefono apre subito l'app di posta; da computer, dove spesso non c'è un'app di
// posta configurata, fa scegliere tra Gmail, Outlook, app di posta o indirizzo da copiare.
const dialog = document.getElementById('beta-dialog');
if (dialog && typeof dialog.showModal === 'function') {
  const form = dialog.querySelector('[data-step="1"]');
  const step2 = dialog.querySelector('[data-step="2"]');
  const input = dialog.querySelector('#beta-name');
  const send = dialog.querySelector('[data-beta-send]');
  const osLabel = dialog.querySelector('[data-os-label]');
  const copyBtn = dialog.querySelector('[data-beta-copy]');
  const copyLabel = copyBtn.textContent;
  const isPhone = window.matchMedia('(hover: none) and (pointer: coarse)').matches;
  let baseHref = '';

  const showStep = (n) => { form.hidden = n !== 1; step2.hidden = n !== 2; };
  const update = () => { send.disabled = input.value.trim().length < 2; };
  input.addEventListener('input', update);

  document.querySelectorAll('.btn-os').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      baseHref = btn.getAttribute('href');
      osLabel.textContent = btn.dataset.os === 'android' ? 'Android' : 'iOS (iPhone)';
      showStep(1);
      update();
      dialog.showModal();
      input.focus();
    });
  });

  dialog.querySelector('[data-beta-cancel]').addEventListener('click', () => dialog.close());
  dialog.querySelector('[data-beta-back]').addEventListener('click', () => { showStep(1); input.focus(); });
  dialog.addEventListener('click', (e) => { if (e.target === dialog) dialog.close(); });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = input.value.trim().replace(/\s+/g, ' ');
    if (name.length < 2) return;
    const href = baseHref + encodeURIComponent(name);
    if (isPhone) { window.location.href = href; dialog.close(); return; }

    // mailto:indirizzo?subject=…&body=…  →  link di composizione per Gmail e Outlook sul web.
    const url = new URL(href);
    const to = decodeURIComponent(url.pathname);
    const subject = url.searchParams.get('subject') || '';
    const body = url.searchParams.get('body') || '';
    const q = (pairs) => pairs.map(([k, v]) => k + '=' + encodeURIComponent(v)).join('&');
    dialog.querySelector('[data-beta-gmail]').href =
      'https://mail.google.com/mail/?' + q([['view', 'cm'], ['fs', '1'], ['to', to], ['su', subject], ['body', body]]);
    dialog.querySelector('[data-beta-outlook]').href =
      'https://outlook.live.com/mail/0/deeplink/compose?' + q([['to', to], ['subject', subject], ['body', body]]);
    dialog.querySelector('[data-beta-app]').href = href;
    dialog.querySelector('[data-beta-subject]').textContent = subject;
    copyBtn.textContent = copyLabel;
    copyBtn.dataset.address = to;
    showStep(2);
  });

  copyBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(copyBtn.dataset.address);
      copyBtn.textContent = copyBtn.dataset.copied;
    } catch (err) { /* appunti non disponibili: l'indirizzo resta visibile e selezionabile */ }
  });
}
