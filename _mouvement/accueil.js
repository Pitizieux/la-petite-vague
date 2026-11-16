/* La petite vague — motion design, avec Motion (la bibliothèque Framer Motion,
   dans sa version sans React).

   Ce fichier est la SOURCE de la page d'accueil, qui charge /accueil.js, fabriqué à partir d'ici
   (les autres pages gardent /mouvement.js, fabriqué depuis source.js) :
       cd _mouvement && npm install && npm run build

   Principes :
   - Tout est un plus. La page pose la classe « mo » sur <html> seulement si le
     JavaScript tourne et que le système accepte le mouvement ; sans elle, on ne
     fait rien et rien n'est caché. Si ce fichier plante, on retire la classe.
   - On ne réécrit jamais les textes : les titres sont seulement enveloppés, ligne
     par ligne, au moment de l'animation. */

import { animate, scroll, stagger, press } from 'motion';

(function () {
  var doc = document.documentElement;
  if (!doc.classList.contains('mo')) return;
  window.LPV_mo = true;

  var DOUX = [0.22, 1, 0.36, 1];
  var RESSORT = { type: 'spring', bounce: 0.2, visualDuration: 0.8 };
  var VIF = { type: 'spring', bounce: 0.4, visualDuration: 0.55 };
  var petit = window.matchMedia('(max-width: 899px)').matches;

  function tous(sel, racine) { return [].slice.call((racine || document).querySelectorAll(sel)); }
  function nettoyer(els, props) {
    (els.length === undefined ? [els] : els).forEach(function (el) {
      (props || ['opacity', 'transform', 'clip-path', 'will-change']).forEach(function (p) { el.style.removeProperty(p); });
    });
  }

  try {

    /* ——— 1. L'ouverture : le nom monte mot à mot, la photo arrive avec la houle ——— */
    var acc = document.querySelector('.accroche');
    if (acc) {
      var nom = acc.querySelector('.h1-nom'), mots = [];
      (function decouper(el) {
        [].slice.call(el.childNodes).forEach(function (n) {
          if (n.nodeType === 3) {
            var morceaux = n.nodeValue.split(/(\s+)/), frag = document.createDocumentFragment();
            morceaux.forEach(function (m) {
              if (!m) return;
              if (/^\s+$/.test(m)) { frag.appendChild(document.createTextNode(m)); return; }
              var o = document.createElement('span'), i = document.createElement('span');
              o.className = 'mot'; i.textContent = m; o.appendChild(i); frag.appendChild(o); mots.push(i);
            });
            el.replaceChild(frag, n);
          } else if (n.nodeType === 1 && n.nodeName !== 'BR') { decouper(n); }
        });
      })(nom);

      var bas = tous('.accroche-bas > p, .repere, .actions', acc);
      var photo = acc.querySelector('.accroche-photo'), houle = acc.querySelector('.houle');
      var entete = document.getElementById('entete');

      animate(acc.querySelector('.chapeau'), { opacity: [0, 1], y: [14, 0] }, { duration: 0.8, ease: DOUX, delay: 0.1 });
      animate(mots, { y: ['112%', '0%'], rotate: [5, 0] },
        { duration: 1.25, ease: DOUX, delay: stagger(0.11, { startDelay: 0.18 }) });
      animate(bas, { opacity: [0, 1], y: [26, 0] },
        { duration: 0.9, ease: DOUX, delay: stagger(0.1, { startDelay: 0.75 }) })
        .then(function () { nettoyer(bas); });
      if (photo) {
        animate(photo, { y: [90, 0], opacity: [0, 1] },
          { duration: 1.5, ease: DOUX, delay: 0.35, opacity: { duration: 0.6, delay: 0.35 } })
          .then(function () { nettoyer(photo); });
        if (houle) animate(houle, { scaleY: [3, 1] }, { duration: 1.9, ease: DOUX, delay: 0.35 });
        houle && (houle.style.transformOrigin = '50% 0');
      }
      if (entete) animate(entete, { opacity: [0, 1] }, { duration: 0.8, delay: 0.5 })
        .then(function () { entete.style.removeProperty('opacity'); });
      // le trait du logo se dessine
      tous('.entete .marque svg path').forEach(function (p, k) {
        try {
          var l = p.getTotalLength();
          p.style.strokeDasharray = l;
          animate(p, { strokeDashoffset: [l, 0] }, { duration: 1.4, ease: DOUX, delay: 0.5 + k * 0.18 })
            .then(function () { p.style.removeProperty('stroke-dasharray'); p.style.removeProperty('stroke-dashoffset'); });
        } catch (e) {}
      });
      acc.classList.add('vu');

      // en quittant le haut de page : la photo glisse moins vite que la page
      if (photo) {
        var imgs = tous('img', photo);
        scroll(function (p) {
          var y = (62 - p * 34).toFixed(1) + '%';
          imgs.forEach(function (im) { im.style.objectPosition = '50% ' + y; });
        }, { target: photo, offset: ['start end', 'end start'] });
      }
    }

    /* ——— 2. Les révélations au défilement ——— */
    function lignes(h) {
      var groupes = [[]];
      [].slice.call(h.childNodes).forEach(function (n) {
        if (n.nodeName === 'BR') groupes.push([]); else groupes[groupes.length - 1].push(n);
      });
      h.textContent = '';
      return groupes.map(function (g) {
        var o = document.createElement('span'), i = document.createElement('span');
        o.className = 'ligne';
        g.forEach(function (n) { i.appendChild(n); });
        o.appendChild(i); h.appendChild(o);
        return i;
      });
    }

    function compter(b, delai) {
      var n = b && b.firstChild;
      if (!n || n.nodeType !== 3) return;
      var original = n.nodeValue, m = original.match(/^(\s*)(\d+)/);
      if (!m) return;
      var cible = parseInt(m[2], 10);
      if (cible < 5) return;
      var debut = m[1], reste = original.slice(m[0].length);
      n.nodeValue = debut + '0' + reste;
      animate(0, cible, {
        duration: 1.6, ease: DOUX, delay: delai,
        onUpdate: function (v) { n.nodeValue = debut + Math.round(v) + reste; },
        onComplete: function () { n.nodeValue = original; }
      });
    }

    function reveler(el, delai) {
      var genre = el.getAttribute('data-r');
      if (genre === 'titre') {
        var ins = lignes(el);
        animate(ins, { y: ['108%', '0%'] }, { duration: 1.1, ease: DOUX, delay: stagger(0.11, { startDelay: delai }) })
          .then(function () { nettoyer(ins); });
      } else if (genre === 'photo') {
        animate(el, { clipPath: ['inset(100% 0% 0% 0%)', 'inset(0% 0% 0% 0%)'], scale: [1.12, 1] },
          { duration: 1.4, ease: DOUX, delay: delai })
          .then(function () { nettoyer(el); });
      } else if (genre === 'liste') {
        var enfants = [].slice.call(el.children);
        animate(enfants, { opacity: [0, 1], y: [24, 0] },
          { duration: 0.85, ease: DOUX, delay: stagger(0.07, { startDelay: delai }) })
          .then(function () { nettoyer(enfants); });
        if (el.classList.contains('chiffres')) {
          enfants.forEach(function (c, k) { compter(c.querySelector('b'), delai + k * 0.07); });
        }
      } else {
        animate(el, { opacity: [0, 1], y: [28, 0] }, { duration: 0.95, ease: DOUX, delay: delai })
          .then(function () { nettoyer(el); });
      }
      el.classList.add('vu');
    }

    var cibles = tous('[data-r]');
    if ('IntersectionObserver' in window) {
      var oeil = new IntersectionObserver(function (entrees) {
        var lot = entrees.filter(function (e) { return e.isIntersecting; })
          .map(function (e) { oeil.unobserve(e.target); return e.target; })
          .sort(function (a, b) {
            return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
          });
        lot.forEach(function (el, k) { reveler(el, Math.min(k * 0.09, 0.45)); });
      }, { rootMargin: '0px 0px -7% 0px', threshold: 0.06 });
      cibles.forEach(function (el) { oeil.observe(el); });
    } else {
      cibles.forEach(function (el) { el.classList.add('vu'); });
    }

    // les cinq étoiles de l'avis s'allument une à une
    var etoiles = tous('.citation .etoiles b');
    if (etoiles.length && 'IntersectionObserver' in window) {
      etoiles.forEach(function (e) { e.style.opacity = '0'; });
      var oe = new IntersectionObserver(function (en) {
        if (!en[0].isIntersecting) return;
        oe.disconnect();
        animate(etoiles, { opacity: [0, 1], scale: [0, 1], rotate: [-40, 0] },
          { delay: stagger(0.09, { startDelay: 0.35 }), opacity: { duration: 0.2 }, scale: VIF, rotate: VIF })
          .then(function () { nettoyer(etoiles); });
      }, { threshold: 0.6 });
      oe.observe(etoiles[0].parentNode);
    }

    /* ——— 3. Profondeur : les photos ne défilent pas toutes à la même vitesse ——— */
    tous('[data-para]').forEach(function (el) {
      var a = parseFloat(el.getAttribute('data-para')) * (petit ? 0.35 : 1);
      scroll(animate(el, { y: [a, -a] }, { ease: 'linear' }), { target: el, offset: ['start end', 'end start'] });
    });
    tous('[data-bandeau] img').forEach(function (im) {
      scroll(function (p) { im.style.objectPosition = '50% ' + (22 + p * 56).toFixed(1) + '%'; },
        { target: im, offset: ['start end', 'end start'] });
    });
    var signature = document.querySelector('.signature'), pied = document.querySelector('.pied');
    if (signature && pied) {
      scroll(animate(signature, { x: ['-9%', '0%'], opacity: [0.2, 1] }, { ease: 'linear' }),
        { target: pied, offset: ['start end', 'end end'] });
    }

    /* ——— 4. « Une journée ici » : la scène reste à l'écran, le soleil traverse le ciel ——— */
    var j = document.getElementById('journee');
    if (j && window.innerHeight >= 540 && CSS.supports('position', 'sticky')) {
      var moments = tous('.moment', j), soleil = j.querySelector('.soleil'), ciel = j.querySelector('.ciel'),
          crans = tous('.journee-pas i', j);
      var teintes = [[220, 229, 229], [244, 239, 231], [243, 220, 200]];   // matin, midi, soir
      var courant = -1;
      j.classList.add('scene'); moments[0].classList.add('actif');
      scroll(function (p) {
        // le soleil sur son arc (même courbe que le tracé pointillé)
        var t = 0.07 + 0.86 * p, L = ciel.clientWidth, H = ciel.clientHeight;
        var y = (190 - 680 * t * (1 - t)) / 200 * H;
        soleil.style.transform = 'translate3d(' + (t * L).toFixed(1) + 'px,' + y.toFixed(1) + 'px,0)';
        // la couleur du ciel
        var q = Math.min(0.9999, Math.max(0, p)) * 2, k0 = Math.floor(q), f = q - k0;
        var c = teintes[k0].map(function (v, n) { return Math.round(v + (teintes[k0 + 1][n] - v) * f); });
        j.style.backgroundColor = 'rgb(' + c.join(',') + ')';
        // le moment affiché
        var k = Math.min(2, Math.floor(p * 3));
        if (k !== courant) {
          courant = k;
          moments.forEach(function (m, n) {
            m.classList.toggle('actif', n === k);
            m.classList.toggle('passe', n < k);
          });
        }
        crans.forEach(function (i, n) { i.style.setProperty('--p', Math.min(1, Math.max(0, p * 3 - n)).toFixed(3)); });
      }, { target: j, offset: ['start start', 'end end'] });
    }

    /* ——— 5. Les gestes : boutons, sommaire, visionneuse, onglets ——— */
    press('.bouton, .rond, .sommaire', function (el) {
      el.style.transition = 'none';
      animate(el, { scale: 0.95 }, { type: 'spring', stiffness: 700, damping: 30 });
      return function () {
        animate(el, { scale: 1 }, { type: 'spring', stiffness: 500, damping: 15 }).then(function () {
          el.style.removeProperty('transform');
          requestAnimationFrame(function () { el.style.removeProperty('transition'); });
        });
      };
    });

    var menu = document.getElementById('menu');
    if (menu) {
      new MutationObserver(function () {
        if (menu.hidden) return;
        animate(menu, { clipPath: ['inset(0% 0% 100% 0%)', 'inset(0% 0% 0% 0%)'] }, { duration: 0.6, ease: DOUX })
          .then(function () { menu.style.removeProperty('clip-path'); });
        animate(tous('li', menu), { opacity: [0, 1], y: [34, 0] },
          { duration: 0.7, ease: DOUX, delay: stagger(0.045, { startDelay: 0.16 }) });
      }).observe(menu, { attributes: true, attributeFilter: ['hidden'] });
    }

    var vis = document.getElementById('visionneuse');
    if (vis) {
      var grande = vis.querySelector('img'), sens = 0, ouverte = false;
      vis.querySelector('.precedent').addEventListener('click', function () { sens = -1; }, true);
      vis.querySelector('.suivant').addEventListener('click', function () { sens = 1; }, true);
      document.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') sens = -1;
        if (e.key === 'ArrowRight') sens = 1;
      }, true);
      vis.addEventListener('touchend', function (e) { sens = 2; }, true);
      new MutationObserver(function () {
        var o = vis.classList.contains('ouverte');
        if (o && !ouverte) {
          sens = 0;
          animate(vis, { opacity: [0, 1] }, { duration: 0.3, ease: 'easeOut' });
          animate(grande, { opacity: [0, 1], scale: [0.92, 1], y: [22, 0] }, VIF);
        }
        ouverte = o;
      }).observe(vis, { attributes: true, attributeFilter: ['class'] });
      new MutationObserver(function () {
        if (!ouverte || !sens || !grande.getAttribute('src')) return;
        var d = sens === 2 ? 0 : sens;
        animate(grande, { opacity: [0, 1], x: [d * 70, 0], scale: [0.97, 1] },
          { opacity: { duration: 0.35 }, x: VIF, scale: VIF });
        sens = 0;
      }).observe(grande, { attributes: true, attributeFilter: ['src'] });
    }

    var env = document.getElementById('environs'), premier = true;
    if (env) {
      env.addEventListener('lpv:onglet', function (e) {
        if (premier) { premier = false; return; }            // pas d'animation au chargement
        var volet = e.detail;
        var morceaux = tous('li, .yeu-corps > div, .yeu > .lien-ot', volet);
        animate(morceaux, { opacity: [0, 1], y: [22, 0] },
          { duration: 0.7, ease: DOUX, delay: stagger(0.06) })
          .then(function () { nettoyer(morceaux); });
      });
      setTimeout(function () { premier = false; }, 1500);
    }

  } catch (erreur) {
    // quoi qu'il arrive, le contenu reste lisible
    doc.classList.remove('mo');
    if (window.console) console.error(erreur);
  }
})();
