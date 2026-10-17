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
const dialog = document.getElementById('beta-dialog');
if (dialog && typeof dialog.showModal === 'function') {
  const input = dialog.querySelector('#beta-name');
  const send = dialog.querySelector('[data-beta-send]');
  const osLabel = dialog.querySelector('[data-os-label]');
  let baseHref = '';

  const update = () => { send.disabled = input.value.trim().length < 2; };
  input.addEventListener('input', update);

  document.querySelectorAll('.btn-os').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      baseHref = btn.getAttribute('href');
      osLabel.textContent = btn.dataset.os === 'android' ? 'Android' : 'iOS (iPhone)';
      update();
      dialog.showModal();
      input.focus();
    });
  });

  dialog.querySelector('[data-beta-cancel]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (e) => { if (e.target === dialog) dialog.close(); });

  dialog.querySelector('form').addEventListener('submit', (e) => {
    const name = input.value.trim().replace(/\s+/g, ' ');
    if (name.length < 2) { e.preventDefault(); return; }
    window.location.href = baseHref + encodeURIComponent(name);
  });
}
