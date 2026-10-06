# -*- coding: utf-8 -*-
"""Insère la traduction anglaise dans index.html.

    cd _traduction && python3 gen.py

Lit en.py, fabrique le bloc JavaScript et le remplace entre les deux
balises TRADUCTION:DEBUT / TRADUCTION:FIN dans index.html.
Ne touche à rien d'autre dans le fichier.
"""
import json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from en import EN, META, UI

PAGE = os.path.join(ICI, '..', 'index.html')
DEBUT = '<!-- TRADUCTION:DEBUT — bloc produit par _traduction/gen.py, ne pas modifier à la main -->'
FIN = '<!-- TRADUCTION:FIN -->'

dico = json.dumps(EN, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
meta = json.dumps(META, ensure_ascii=False, separators=(',', ':'))
ui = json.dumps(UI, ensure_ascii=False, separators=(',', ':'))

JS = f'''{DEBUT}
<script>
/* Bascule français / anglais.

   Le français est écrit en dur dans la page ; l'anglais vit dans le
   dictionnaire ci-dessous, dont chaque clé est la phrase française EXACTE.
   Si vous modifiez un texte français dans la page, modifiez la clé
   correspondante : sinon la phrase restera en français en version anglaise.
   La console du navigateur affiche la liste des clés orphelines.

   Pour régénérer ce bloc : cd _traduction && python3 gen.py */
(function(){{
  var EN = {dico};
  var META = {meta};
  var UI = {ui};

  var html = document.documentElement;
  var boutons = [].slice.call(document.querySelectorAll('.langue'));
  var origines = null;          // [élément|nœud, attribut|null, valeur française]
  var langue = 'fr';

  function clef(v){{ return (v || '').replace(/\\s+/g, ' ').trim(); }}

  /* On relève une fois pour toutes ce qui est traduisible, en gardant
     la valeur française pour pouvoir revenir en arrière. */
  function relever(){{
    var liste = [];
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    var n;
    while ((n = w.nextNode())){{
      var p = n.parentElement;
      if (!p || p.closest('script,style')) continue;
      var k = clef(n.nodeValue);
      if (k && Object.prototype.hasOwnProperty.call(EN, k)) liste.push([n, null, n.nodeValue, EN[k]]);
    }}
    ['alt','aria-label','title'].forEach(function(a){{
      [].forEach.call(document.querySelectorAll('[' + a + ']'), function(el){{
        var v = el.getAttribute(a), k = clef(v);
        if (!k) return;
        if (Object.prototype.hasOwnProperty.call(EN, k)){{ liste.push([el, a, v, EN[k]]); return; }}
        /* « Agrandir : <description> » est fabriqué par le script de la
           visionneuse : on traduit le préfixe et la description séparément. */
        if (k.indexOf('Agrandir : ') === 0){{
          var reste = clef(k.slice(11));
          if (Object.prototype.hasOwnProperty.call(EN, reste))
            liste.push([el, a, v, UI.agrandir + EN[reste]]);
        }}
      }});
    }});
    return liste;
  }}

  function metaSet(sel, valeur){{
    var e = document.querySelector(sel);
    if (e) e.setAttribute('content', valeur);
  }}

  function poser(l){{
    if (l === langue) return;
    if (!origines) origines = relever();
    var vers = (l === 'en');
    origines.forEach(function(o){{
      var cible = o[0], attr = o[1], fr = o[2], en = o[3];
      var v = vers ? en : fr;
      if (vers && attr === null){{
        /* on garde l'espacement d'origine autour du texte */
        v = (/^\\s/.test(fr) ? ' ' : '') + en + (/\\s$/.test(fr) ? ' ' : '');
      }}
      if (attr) cible.setAttribute(attr, v); else cible.nodeValue = v;
    }});
    html.lang = l;
    document.title = vers ? META.titre : META.titre_fr;
    metaSet('meta[name="description"]', vers ? META.description : META.description_fr);
    metaSet('meta[property="og:title"]', vers ? META.og_titre : META.og_titre_fr);
    metaSet('meta[property="og:description"]', vers ? META.og_description : META.og_description_fr);
    metaSet('meta[property="og:locale"]', vers ? 'en_GB' : 'fr_FR');
    boutons.forEach(function(b){{
      b.setAttribute('lang', vers ? 'fr' : 'en');
      b.setAttribute('aria-label', vers ? 'Lire cette page en français' : 'Read this page in English');
      b.setAttribute('title', vers ? 'Français' : 'English');
    }});
    window.LPV_LANGUE = langue = l;
    try {{ localStorage.setItem('lpv-langue', l); }} catch (e) {{}}
    try {{
      var u = new URL(location.href);
      if (vers) u.searchParams.set('lang', 'en'); else u.searchParams.delete('lang');
      history.replaceState(null, '', u.pathname + u.search + u.hash);
    }} catch (e) {{}}
  }}

  /* Le français de départ, pour pouvoir y revenir. */
  META.titre_fr = document.title;
  ['description_fr','og_titre_fr','og_description_fr'].forEach(function(c, i){{
    var sel = ['meta[name="description"]','meta[property="og:title"]','meta[property="og:description"]'][i];
    var e = document.querySelector(sel);
    META[c] = e ? e.getAttribute('content') : '';
  }});

  boutons.forEach(function(b){{
    b.setAttribute('lang', 'en');
    b.setAttribute('aria-label', 'Read this page in English');
    b.setAttribute('title', 'English');
    b.addEventListener('click', function(){{ poser(langue === 'fr' ? 'en' : 'fr'); }});
  }});

  /* Choix au chargement : ce que le visiteur a déjà choisi, sinon l'adresse,
     sinon la langue du navigateur. */
  var voulu = null;
  try {{ voulu = localStorage.getItem('lpv-langue'); }} catch (e) {{}}
  if (!voulu){{
    var p = new URLSearchParams(location.search).get('lang');
    if (p === 'en' || p === 'fr') voulu = p;
    else if (location.hash === '#en') voulu = 'en';
    else if (!/^fr/i.test(navigator.language || 'fr')) voulu = 'en';
  }}
  if (voulu === 'en') poser('en');

  /* Aide à la maintenance : signale les textes français que le dictionnaire
     ne connaît pas (visible seulement dans la console du navigateur). */
  window.LPV_ORPHELINS = function(){{
    if (langue !== 'fr') return ['Repassez la page en français avant de lancer ce test.'];
    var m = [], w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false), n;
    while ((n = w.nextNode())){{
      var p = n.parentElement;
      if (!p || p.closest('script,style')) continue;
      var k = clef(n.nodeValue);
      if (!k || k.length <= 3) continue;
      if (/^[\\d\\s.,:°+\\/-]+$/.test(k)) continue;
      if (Object.prototype.hasOwnProperty.call(EN, k)) continue;
      if (m.indexOf(k) < 0) m.push(k);
    }}
    return m;
  }};
}})();
</script>
{FIN}'''

s = open(PAGE, encoding='utf-8').read()
if DEBUT in s:
    s = re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN), lambda _: JS, s, flags=re.S)
else:
    s = s.replace('\n</body>', '\n' + JS + '\n</body>', 1)
open(PAGE, 'w', encoding='utf-8').write(s)
print('bloc de traduction inséré :', len(EN), 'phrases,', round(len(JS) / 1024), 'Ko')
