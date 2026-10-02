/* Манго — общий скрипт для всех страниц.
   Анимации на GSAP + ScrollTrigger, плавная прокрутка на Lenis (оба с CDN).
   Если библиотеки не загрузились или включено «уменьшить движение», сайт просто статичный
   и весь контент виден: начальные состояния анимаций задаёт только JS. */

const CONTACTS = {
  telegram: 'mango_studio',        // ник без @
  whatsapp: '79000000000',         // номер без плюса и пробелов — ЗАМЕНИТЬ на реальный
  message: 'Здравствуйте! Хочу записаться на консультацию по проекту.',
};

const tgUrl = `https://t.me/${CONTACTS.telegram}`;
const waUrl = `https://wa.me/${CONTACTS.whatsapp}?text=${encodeURIComponent(CONTACTS.message)}`;
document.querySelectorAll('[data-tg]').forEach(a => { a.href = tgUrl; });
document.querySelectorAll('[data-wa]').forEach(a => { a.href = waUrl; });
document.querySelectorAll('[data-tg-name]').forEach(el => { el.textContent = '@' + CONTACTS.telegram; });

const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const finePointer = matchMedia('(pointer: fine)').matches;
const hasGsap = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';
const motion = hasGsap && !reduce;
let lenis = null;

/* ── окно «Записаться»: раскрывается от нажатой кнопки ── */
const modal = document.getElementById('book');
if (modal) {
  const open = (from) => {
    if (typeof modal.showModal !== 'function') return false;
    if (modal.open) modal.close();
    modal.showModal();
    lenis && lenis.stop();
    if (motion && from) {
      const r = from.getBoundingClientRect();
      const m = modal.getBoundingClientRect();
      gsap.fromTo(modal,
        { x: r.left + r.width / 2 - (m.left + m.width / 2), y: r.top + r.height / 2 - (m.top + m.height / 2), scale: .25, opacity: 0 },
        { x: 0, y: 0, scale: 1, opacity: 1, duration: .6, ease: 'expo.out' });
      gsap.fromTo(modal.querySelectorAll('.modal-in > *'), { y: 16, opacity: 0 },
        { y: 0, opacity: 1, duration: .5, stagger: .05, delay: .12, ease: 'power3.out' });
    }
    return true;
  };
  const close = () => modal.close();
  document.querySelectorAll('[data-book]').forEach(btn => {
    btn.addEventListener('click', e => { if (open(btn)) e.preventDefault(); });
  });
  modal.querySelector('.modal-x').addEventListener('click', close);
  modal.addEventListener('click', e => { if (e.target === modal) close(); });
  modal.addEventListener('close', () => lenis && lenis.start());
  modal.querySelectorAll('.msg').forEach(a => a.addEventListener('click', close));
}

/* ── мобильное меню ── */
const burger = document.getElementById('burger');
const nav = document.getElementById('nav');
if (burger && nav) {
  const setMenu = (open) => {
    nav.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.innerHTML = open ? '<i class="ph ph-x" aria-hidden="true"></i>' : '<i class="ph ph-list" aria-hidden="true"></i>';
    if (lenis) open ? lenis.stop() : lenis.start();
    if (open && motion) {
      gsap.fromTo(nav.querySelectorAll('a'), { y: 40, opacity: 0 },
        { y: 0, opacity: 1, duration: .6, stagger: .06, delay: .15, ease: 'expo.out' });
    }
  };
  burger.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
}

/* ── заливка кнопки начинается с точки, где в неё вошёл курсор ── */
document.querySelectorAll('.btn-acc').forEach(b => {
  b.addEventListener('pointerenter', e => {
    const r = b.getBoundingClientRect();
    b.style.setProperty('--hx', `${e.clientX - r.left}px`);
    b.style.setProperty('--hy', `${e.clientY - r.top}px`);
  });
});

/* ── подсветка плиток под курсором ── */
document.querySelectorAll('.tile').forEach(t => {
  t.addEventListener('pointermove', e => {
    const r = t.getBoundingClientRect();
    t.style.setProperty('--mx', `${e.clientX - r.left}px`);
    t.style.setProperty('--my', `${e.clientY - r.top}px`);
  });
});

if (motion) initMotion();

function initMotion() {
  gsap.registerPlugin(ScrollTrigger);

  /* плавная прокрутка */
  if (window.Lenis) {
    lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length > 1 && document.querySelector(id)) { e.preventDefault(); lenis.scrollTo(id, { offset: -90 }); }
    }));
  }

  /* шапка: фон после начала прокрутки, прячется при прокрутке вниз, полоса прогресса */
  const head = document.querySelector('.head');
  const prog = document.querySelector('.prog');
  ScrollTrigger.create({
    start: 0, end: 'max',
    onUpdate: self => {
      const y = self.scroll();
      head.classList.toggle('scrolled', y > 20);
      head.classList.toggle('hidden', self.direction === 1 && y > 500 && !nav.classList.contains('open'));
      if (prog) prog.style.transform = `scaleX(${self.progress})`;
    },
  });

  /* заголовки поднимаются по словам: .split */
  document.querySelectorAll('.split').forEach(el => {
    splitWords(el, 'w');
    const inHero = el.closest('.hero, .page-hero');
    gsap.from(el.querySelectorAll('.w > span'), {
      yPercent: 115, rotate: 5, duration: 1.1, stagger: .06, ease: 'expo.out', delay: inHero ? .15 : 0,
      scrollTrigger: inHero ? null : { trigger: el, start: 'top 85%', once: true },
    });
  });

  /* титульный блок главной */
  const hero = document.querySelector('.hero');
  if (hero) {
    gsap.timeline({ delay: .35 })
      .from('.fruit', { scale: .3, rotate: -50, opacity: 0, duration: 1.6, ease: 'elastic.out(1,.55)' }, 0)
      .from('.orbit', { opacity: 0, scale: .7, duration: 1.3, ease: 'expo.out' }, .15)
      .from('.hero .lede', { y: 24, opacity: 0, duration: .9, ease: 'power3.out' }, .45)
      .from('.hero-cta > *', { y: 24, opacity: 0, duration: .8, stagger: .08, ease: 'power3.out' }, .6);
    gsap.to('.fruit svg', { y: -18, duration: 3.2, ease: 'sine.inOut', yoyo: true, repeat: -1 });

    if (finePointer) {
      const art = document.querySelector('.hero-art');
      const qx = gsap.quickTo('.fruit', 'x', { duration: 1, ease: 'power3.out' });
      const qy = gsap.quickTo('.fruit', 'y', { duration: 1, ease: 'power3.out' });
      const qr = gsap.quickTo('.fruit', 'rotate', { duration: 1, ease: 'power3.out' });
      hero.addEventListener('pointermove', e => {
        const r = art.getBoundingClientRect();
        const nx = (e.clientX - (r.left + r.width / 2)) / innerWidth;
        const ny = (e.clientY - (r.top + r.height / 2)) / innerHeight;
        qx(nx * 60); qy(ny * 40); qr(nx * 16);
      });
    }
    gsap.to('.hero-grid', { yPercent: 16, opacity: .15, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
  }

  /* бегущая строка: ускоряется и меняет направление вместе с прокруткой */
  document.querySelectorAll('.marquee').forEach(m => {
    const loop = gsap.to(m.querySelector('.marquee-track'), { xPercent: -50, duration: 32, ease: 'none', repeat: -1 });
    ScrollTrigger.create({
      trigger: m, start: 'top bottom', end: 'bottom top',
      onUpdate: self => {
        const dir = self.direction;
        const boost = Math.min(Math.abs(self.getVelocity()) / 250, 6);
        gsap.timeline({ overwrite: true })
          .to(loop, { timeScale: dir * (1 + boost), duration: .25 })
          .to(loop, { timeScale: dir, duration: 1.2 });
      },
    });
  });

  /* появление блоков: [data-reveal] и группы [data-stagger] */
  gsap.utils.toArray('[data-reveal]').forEach(el => {
    gsap.from(el, { y: 60, opacity: 0, duration: 1.1, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 88%', once: true } });
  });
  gsap.utils.toArray('[data-stagger]').forEach(group => {
    gsap.from(group.children, {
      y: 70, opacity: 0, duration: 1, stagger: .08, ease: 'expo.out',
      scrollTrigger: { trigger: group, start: 'top 85%', once: true },
    });
  });

  /* параллакс: [data-speed] */
  gsap.utils.toArray('[data-speed]').forEach(el => {
    gsap.to(el, { yPercent: parseFloat(el.dataset.speed) * -100, ease: 'none',
      scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* манифест проявляется по словам вместе с прокруткой */
  document.querySelectorAll('.manifest p').forEach(p => {
    splitWords(p, 'mw');
    gsap.fromTo(p.querySelectorAll('.mw'), { opacity: .14 }, {
      opacity: 1, stagger: .1, ease: 'none',
      scrollTrigger: { trigger: p, start: 'top 78%', end: 'bottom 45%', scrub: true },
    });
  });

  /* счётчики фактов */
  document.querySelectorAll('[data-count]').forEach(el => {
    const end = parseInt(el.dataset.count, 10);
    const obj = { v: 0 };
    el.firstChild.nodeValue = '0';
    gsap.to(obj, {
      v: end, duration: 1.6, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 90%', once: true },
      onUpdate: () => { el.firstChild.nodeValue = Math.round(obj.v).toLocaleString('ru-RU'); },
      onComplete: () => { el.firstChild.nodeValue = end.toLocaleString('ru-RU'); },
    });
  });

  /* этапы: предыдущая карточка уходит вглубь, когда на неё наезжает следующая */
  const cards = gsap.utils.toArray('.stack-card');
  cards.forEach((card, i) => {
    card.style.setProperty('--i', i);
    const next = cards[i + 1];
    if (!next) return;
    gsap.to(card, {
      scale: .92 + i * .015, ease: 'none',
      scrollTrigger: { trigger: next, start: 'top bottom', end: 'top 30%', scrub: true },
    });
  });

  /* горизонтальная лента кейса: секция закрепляется, прокрутка двигает ленту вбок */
  gsap.matchMedia().add('(min-width: 900px)', () => {
    document.querySelectorAll('.hpan').forEach(wrap => {
      const track = wrap.querySelector('.hpan-track');
      const dist = () => track.scrollWidth - innerWidth;
      gsap.to(track, {
        x: () => -dist(), ease: 'none',
        scrollTrigger: { trigger: wrap, start: 'center center', end: () => '+=' + dist(), pin: true, scrub: 1, invalidateOnRefresh: true },
      });
    });
  });

  /* полосы «созревания» и цвета палитры вырастают слева направо */
  gsap.utils.toArray('.page-hero .ripen').forEach(el => gsap.from(el, { scaleX: 0, duration: 1.6, delay: .5, ease: 'expo.out' }));
  gsap.utils.toArray('.swatches').forEach(g => {
    gsap.from(g.children, { scaleX: 0, duration: 1.2, stagger: .09, ease: 'expo.out', scrollTrigger: { trigger: g, start: 'top 85%', once: true } });
  });

  /* плоды в финальном призыве поворачиваются при прокрутке */
  gsap.utils.toArray('.final-mango').forEach((el, i) => {
    gsap.to(el, { rotate: i ? -60 : 70, yPercent: i ? -30 : 30, ease: 'none',
      scrollTrigger: { trigger: el.closest('.final'), start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* кнопки тянутся к курсору */
  if (finePointer) {
    document.querySelectorAll('.mag').forEach(b => {
      const qx = gsap.quickTo(b, 'x', { duration: .5, ease: 'power3.out' });
      const qy = gsap.quickTo(b, 'y', { duration: .5, ease: 'power3.out' });
      b.addEventListener('pointermove', e => {
        const r = b.getBoundingClientRect();
        qx((e.clientX - r.left - r.width / 2) * .35);
        qy((e.clientY - r.top - r.height / 2) * .45);
      });
      b.addEventListener('pointerleave', () => { qx(0); qy(0); });
    });
  }

  /* оглавление подсвечивает текущий раздел: .spy */
  document.querySelectorAll('.spy').forEach(spy => {
    const links = [...spy.querySelectorAll('a')];
    links.forEach(a => {
      const sec = document.querySelector(a.getAttribute('href'));
      if (!sec) return;
      ScrollTrigger.create({
        trigger: sec, start: 'top 45%', end: 'bottom 45%',
        onToggle: self => {
          if (!self.isActive) return;
          links.forEach(l => l.classList.toggle('on', l === a));
          if (spy.scrollWidth > spy.clientWidth) spy.scrollTo({ left: a.offsetLeft - 16, behavior: 'smooth' });
        },
      });
    });
  });

  /* строки цен выезжают по очереди внутри группы */
  gsap.utils.toArray('.pgroup').forEach(g => {
    gsap.from(g.querySelectorAll('.prow'), { x: -30, opacity: 0, duration: .8, stagger: .06, ease: 'expo.out',
      scrollTrigger: { trigger: g, start: 'top 82%', once: true } });
  });

  addEventListener('load', () => ScrollTrigger.refresh());
}

/* разбивает текст элемента на слова, сохраняя вложенные теги вроде <em> */
function splitWords(el, cls) {
  const walk = (node) => {
    [...node.childNodes].forEach(n => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(part => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
          const w = document.createElement('span');
          w.className = cls;
          if (cls === 'w') { const inner = document.createElement('span'); inner.textContent = part; w.appendChild(inner); }
          else w.textContent = part;
          frag.appendChild(w);
        });
        n.replaceWith(frag);
      } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
    });
  };
  walk(el);
}
