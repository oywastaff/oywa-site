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
