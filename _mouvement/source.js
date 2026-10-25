/* La petite vague — animations avec Motion (la bibliothèque Framer Motion,
   dans sa version sans React).

   Ce fichier est la SOURCE. Le site charge /mouvement.js, fabriqué à partir
   d'ici :   cd _mouvement && npm install && npm run build

   Principes :
   - Tout est un plus. Si ce fichier ne se charge pas, les animations CSS
     d'origine de la page prennent le relais ; sans JavaScript, rien n'est caché.
   - Si le système demande des animations réduites, on ne fait rien du tout.
   - On ne découpe jamais les textes en morceaux : la bascule français/anglais
     retrouve les phrases par leur texte exact. */

import { animate, scroll, stagger, press } from 'motion';

(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var doc = document.documentElement;
  doc.classList.add('mo');

  var DOUX = [0.22, 1, 0.36, 1];                       // sortie très amortie
  var RESSORT = { type: 'spring', bounce: 0.22, visualDuration: 0.85 };
  var RESSORT_VIF = { type: 'spring', bounce: 0.38, visualDuration: 0.7 };

  /* ——— 1. Barre de lecture : un fil terracotta qui suit le défilement ——— */
  var fil = document.createElement('div');
  fil.className = 'mo-fil';
  fil.setAttribute('aria-hidden', 'true');
  document.body.appendChild(fil);
  var css = document.createElement('style');
  css.textContent =
    '.mo-fil{position:fixed;top:0;left:0;right:0;height:2px;z-index:60;pointer-events:none;' +
    'background:var(--terre,#9C5231);transform-origin:0 50%;transform:scaleX(0)}' +
    '@media print{.mo-fil{display:none}}';
  document.head.appendChild(css);
  scroll(animate(fil, { scaleX: [0, 1] }, { ease: 'linear' }));

  /* ——— 2. Apparitions au défilement, en cascade et avec du ressort ——— */
  var PAGE_PRINCIPALE = !!window.LPV_apparition;
  var cibles;

  if (PAGE_PRINCIPALE) {
    // La page d'accueil a déjà son propre système (CSS + IntersectionObserver).
    // On le débranche et on reprend la main sur ce qui n'est pas encore apparu.
    window.LPV_apparition.oeil.disconnect();
    cibles = [].filter.call(window.LPV_apparition.cibles, function (el) {
      return !el.classList.contains('vu');
    });
  } else {
    // Les autres pages n'ont rien : on cache nous-mêmes ce qui est sous la ligne
    // de flottaison (ce qui est déjà visible ne bouge pas).
    cibles = [].filter.call(document.querySelectorAll(
      '.titre-bloc, .intro, .chiffres > div, .photo, .semaine > *, .points li, .cout > *,' +
      '.faq details, .reserver .bouton, .note'
    ), function (el) {
      if (el.getBoundingClientRect().top < window.innerHeight * 0.95) return false;
      el.style.opacity = '0';
      el.style.transform = 'translateY(16px)';
      return true;
    });
  }

  function genre(el) {
    if (el.matches('.pf, .galerie figure, .carte-photo, .photo')) return 'photo';
    if (el.matches('.titre-bloc, .citation blockquote')) return 'titre';
    if (el.matches('.chiffres > div')) return 'chiffre';
    return 'texte';
  }

  function terminer(el, inner) {
    if (PAGE_PRINCIPALE) el.classList.add('vu');
    ['opacity', 'transform', 'filter', 'clip-path'].forEach(function (p) {
      el.style.removeProperty(p);
    });
    if (inner) { inner.style.removeProperty('transform'); }
    // On rend la main aux transitions CSS (survol des boutons, etc.) une image plus tard,
    // quand l'élément est déjà dans son état final : aucun saut possible.
    requestAnimationFrame(function () {
      el.style.removeProperty('transition');
      if (inner) inner.style.removeProperty('transition');
    });
  }

  function apparaitre(el, delai) {
    el.style.transition = 'none';           // pas de conflit avec les transitions CSS
    var g = genre(el), anims = [];

    if (g === 'photo') {
      // Rideau : la photo se découvre de bas en haut et remonte doucement.
      var img = el.querySelector('img');
      if (img) {
        img.style.transition = 'none';
        anims.push(animate(img, { scale: [1.14, 1] }, { duration: 1.6, ease: DOUX, delay: delai }));
      }
      anims.push(animate(el, {
        opacity: [0, 1],
        clipPath: ['inset(22% 0% 0% 0%)', 'inset(0% 0% 0% 0%)'],
        y: [48, 0]
      }, {
        delay: delai,
        opacity: { duration: 0.5, ease: 'easeOut' },
        clipPath: { duration: 1.25, ease: DOUX },
        y: RESSORT
      }));
      Promise.all(anims).then(function () { terminer(el, img); });
      return;
    }

    if (g === 'titre') {
      anims.push(animate(el, {
        opacity: [0, 1], y: [34, 0], filter: ['blur(8px)', 'blur(0px)']
      }, {
        delay: delai,
        opacity: { duration: 0.7, ease: 'easeOut' },
        filter: { duration: 0.9, ease: DOUX },
        y: RESSORT
      }));
    } else if (g === 'chiffre') {
      anims.push(animate(el, { opacity: [0, 1], y: [26, 0], scale: [0.9, 1] }, {
        delay: delai, opacity: { duration: 0.5 }, y: RESSORT_VIF, scale: RESSORT_VIF
      }));
      compter(el.querySelector('b'), delai);
    } else {
      anims.push(animate(el, { opacity: [0, 1], y: [24, 0] }, {
        delay: delai, opacity: { duration: 0.6, ease: 'easeOut' }, y: RESSORT
      }));
    }
    Promise.all(anims).then(function () { terminer(el); });
  }

  /* Les chiffres clés défilent jusqu'à leur valeur (« 55 m² », « 15 min »…).
     On modifie le nœud de texte lui-même, sans le remplacer, et on remet
     à la fin la valeur exacte : la traduction le retrouve tel quel. */
  function compter(b, delai) {
    var n = b && b.firstChild;
    if (!n || n.nodeType !== 3) return;
    var original = n.nodeValue, m = original.match(/^(\s*)(\d+)/);
    if (!m) return;
    var cible = parseInt(m[2], 10);
    if (cible < 5) return;                 // « 2 voyageurs » n'a pas besoin de compter
    var debut = m[1], reste = original.slice(m[0].length);
    n.nodeValue = debut + '0' + reste;
    animate(0, cible, {
      duration: 1.4, ease: DOUX, delay: delai + 0.1,
      onUpdate: function (v) { n.nodeValue = debut + Math.round(v) + reste; },
      onComplete: function () { n.nodeValue = original; }
    });
  }

  // On regroupe ce qui entre à l'écran au même moment pour le faire apparaître
  // en cascade, dans l'ordre de lecture.
  if (cibles.length && 'IntersectionObserver' in window) {
    var oeil = new IntersectionObserver(function (entrees) {
      var lot = entrees.filter(function (e) { return e.isIntersecting; })
        .map(function (e) { oeil.unobserve(e.target); return e.target; })
        .sort(function (a, b) {
          return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
        });
      var cascade = stagger(0.08);
      lot.forEach(function (el, i) { apparaitre(el, Math.min(cascade(i, lot.length), 0.56)); });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    cibles.forEach(function (el) { oeil.observe(el); });
  } else {
    cibles.forEach(function (el) { terminer(el); });
  }

  /* ——— 3. Parallaxe des grandes photos ———
     On fait glisser le cadrage de l'image (object-position) pendant le défilement :
     la photo semble bouger moins vite que la page. Aucun débordement possible,
     la mise en page ne bouge pas d'un pixel. */
  [].forEach.call(document.querySelectorAll(
    '.accroche-photo img, .bandeau-photo img, .carte-photo img, .pf-pleine img, .photo img'
  ), function (img) {
    var base, x, dernier = '';
    function lire() {
      img.style.removeProperty('object-position');
      var pos = getComputedStyle(img).objectPosition.split(' ');
      x = pos[0] || '50%';
      base = parseFloat(pos[1]);
      if (isNaN(base) || (pos[1] || '').indexOf('%') < 0) base = 50;
      dernier = '';
    }
    lire();
    window.addEventListener('resize', lire);
    var enTete = !!img.closest('.accroche-photo');
    scroll(function (p) {
      // Accroche : de sa position de départ vers le bas quand on quitte le haut de page.
      // Autres photos : ±14 points autour de leur cadrage pendant toute la traversée.
      var y = enTete ? base + p * 22 : base - 14 + p * 28;
      y = Math.max(0, Math.min(100, y));
      var v = x + ' ' + y.toFixed(1) + '%';
      if (v !== dernier) { img.style.objectPosition = v; dernier = v; }
    }, {
      target: enTete ? img.closest('.accroche-photo') : img,
      offset: enTete ? ['start start', 'end start'] : ['start end', 'end start']
    });
  });

  // Le texte de l'accroche s'efface doucement en remontant.
  var texteAccroche = document.querySelector('.accroche > div');
  if (texteAccroche && window.innerWidth >= 900) {
    scroll(animate(texteAccroche, { opacity: [1, 0.15], y: [0, -60] }, { ease: 'linear' }), {
      target: document.querySelector('.accroche'),
      offset: ['start start', 'end start']
    });
  }

  /* ——— 4. Boutons : une petite pression au clic ou au toucher ——— */
  press('.bouton, .sommaire, .langue', function (el) {
    el.style.transition = 'none';
    animate(el, { scale: 0.95 }, { type: 'spring', stiffness: 700, damping: 30 });
    return function () {
      animate(el, { scale: 1 }, { type: 'spring', stiffness: 500, damping: 15 })
        .then(function () {
          el.style.removeProperty('transform');
          requestAnimationFrame(function () { el.style.removeProperty('transition'); });
        });
    };
  });

  /* ——— 5. Visionneuse de photos ——— */
  var vis = document.getElementById('visionneuse');
  if (vis) {
    var grande = vis.querySelector('img');
    var sens = 0;
    vis.querySelector('.precedent').addEventListener('click', function () { sens = -1; }, true);
    vis.querySelector('.suivant').addEventListener('click', function () { sens = 1; }, true);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') sens = -1;
      if (e.key === 'ArrowRight') sens = 1;
    }, true);

    new MutationObserver(function () {
      if (!vis.classList.contains('ouverte')) return;
      if (vis.dataset.moOuverte) return;
      vis.dataset.moOuverte = '1';
      sens = 0;
      animate(vis, { opacity: [0, 1] }, { duration: 0.3, ease: 'easeOut' });
      animate(grande, { opacity: [0, 1], scale: [0.9, 1], y: [24, 0] }, RESSORT_VIF);
    }).observe(vis, { attributes: true, attributeFilter: ['class'] });

    new MutationObserver(function () {
      if (!vis.classList.contains('ouverte')) { delete vis.dataset.moOuverte; return; }
      if (!sens) return;
      animate(grande, { opacity: [0, 1], x: [sens * 70, 0], scale: [0.97, 1] }, {
        opacity: { duration: 0.35 }, x: RESSORT_VIF, scale: RESSORT_VIF
      });
      sens = 0;
    }).observe(grande, { attributes: true, attributeFilter: ['src'] });
  }

  /* ——— 6. Sommaire mobile : les entrées arrivent l'une après l'autre ——— */
  var menu = document.getElementById('menu');
  if (menu) {
    new MutationObserver(function () {
      if (menu.hidden) return;
      animate(menu, { opacity: [0, 1] }, { duration: 0.25 });
      animate(menu.querySelectorAll('li'), { opacity: [0, 1], x: [-24, 0] }, {
        delay: stagger(0.045, { startDelay: 0.05 }),
        opacity: { duration: 0.4 }, x: RESSORT_VIF
      });
    }).observe(menu, { attributes: true, attributeFilter: ['hidden'] });
  }
})();
