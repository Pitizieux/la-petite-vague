# -*- coding: utf-8 -*-
"""Fabrique la version anglaise du site : /en/index.html.

    cd _traduction && python3 gen.py

Le français reste la page de référence (index.html, écrite à la main).
Ce script lit en.py — un dictionnaire dont chaque clé est une phrase
française EXACTE de index.html — et écrit en/index.html, une vraie page
anglaise que Google peut lire et indexer (balises hreflang de part et
d'autre). Relancez-le après chaque modification de index.html.

Il remplace aussi, dans index.html, le bloc entre TRADUCTION:DEBUT et
TRADUCTION:FIN par un petit script qui renvoie les anciennes adresses
anglaises (?lang=en, #en) vers /en/.

En fin de course, il liste les phrases françaises que le dictionnaire ne
connaît pas encore : ajoutez-les dans en.py puis relancez.
"""
import html, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from en import EN, META, UI

RACINE = os.path.join(ICI, '..')
PAGE = os.path.join(RACINE, 'index.html')
SORTIE = os.path.join(RACINE, 'en', 'index.html')
SITE = 'https://lapetitevague85.com'

DEBUT = '<!-- TRADUCTION:DEBUT — bloc produit par _traduction/gen.py, ne pas modifier à la main -->'
FIN = '<!-- TRADUCTION:FIN -->'

# Noms propres et libellés déjà en anglais : rien à traduire.
NOMS = {'English', 'Read this page in English', 'La petite', 'la petite vague', 'vague',
        'La petite vague — 55 m²', 'Saint-Hilaire-de-Riez', 'Saint-Gilles-Croix-de-Vie',
        '85270 Saint-Hilaire-de-Riez', '223 bis rue Georges Clemenceau', 'haloconcierge.fr',
        '© Google', '— © Google', '46.7046, -1.9509 ·', '55 m²', '110 m²', '15 min'}

TITRE_EN = 'Holiday rental for two in Saint-Hilaire-de-Riez (Vendée) | La petite vague'

RENVOI = f'''{DEBUT}
<script>
/* La version anglaise est une vraie page : /en/. Les anciens liens
   (?lang=en ou #en) y sont renvoyés. Pour régénérer : cd _traduction && python3 gen.py */
(function(){{
  try {{
    var p = new URLSearchParams(location.search).get('lang');
    if (p === 'en' || location.hash === '#en')
      location.replace('/en/' + (location.hash === '#en' ? '' : location.hash));
  }} catch (e) {{}}
}})();
</script>
{FIN}'''


def clef(v):
    return re.sub(r'\s+', ' ', v or '').strip()


def traduire_texte(brut, manquants):
    k = clef(html.unescape(brut))
    if not k:
        return brut
    if k in EN:
        avant = re.match(r'^\s*', brut).group(0)
        apres = re.search(r'\s*$', brut).group(0)
        return avant + html.escape(EN[k], quote=False) + apres
    if len(k) > 3 and k not in NOMS and not re.fullmatch(r'[\d\s.,:°+/×–—-]+', k):
        manquants.add(k)
    return brut


def traduire_balise(balise, manquants):
    def attr(m):
        v = html.unescape(m.group(3))
        k = clef(v)
        if k in EN:
            return m.group(1) + m.group(2) + '="' + html.escape(EN[k], quote=True) + '"'
        if len(k) > 3 and k not in NOMS:
            manquants.add(k)
        return m.group(0)
    balise = re.sub(r'(\s)(alt|aria-label|title)="([^"]*)"', attr, balise)
    # chemins relatifs des photos et vidéos : la page vit un dossier plus bas
    balise = re.sub(r'(\s(?:src|data-src|poster|href|srcset)=")(photos|media)/', r'\1/\2/', balise)
    balise = re.sub(r'(,\s*)(photos|media)/', r'\1/\2/', balise)  # srcset multiples
    return balise


def traduire_corps(s, manquants):
    morceaux = re.split(r'(<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>|<[^>]+>)', s, flags=re.S)
    sortie = []
    for i, m in enumerate(morceaux):
        if i % 2 == 0:
            sortie.append(traduire_texte(m, manquants))
        elif m.startswith('<!--') or m.startswith('<style'):
            sortie.append(m)
        elif m.startswith('<script'):
            # libellé posé par la visionneuse photo
            sortie.append(m.replace("'Agrandir : '", "'" + UI['agrandir'] + "'"))
        else:
            sortie.append(traduire_balise(m, manquants))
    return ''.join(sortie)


def meta(s, sel, valeur):
    motif = r'(<meta ' + sel + r' content=")[^"]*(")'
    return re.sub(motif, lambda m: m.group(1) + html.escape(valeur, quote=True) + m.group(2), s, count=1)


# 1. Page française : renvoi des anciennes adresses anglaises
fr = open(PAGE, encoding='utf-8').read()
if DEBUT in fr:
    fr = re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN), lambda _: RENVOI, fr, flags=re.S)
else:
    fr = fr.replace('\n</body>', '\n' + RENVOI + '\n</body>', 1)
open(PAGE, 'w', encoding='utf-8').write(fr)

# 2. Page anglaise
fin_tete = fr.index('</head>')
tete, corps = fr[:fin_tete], fr[fin_tete:]
corps = re.sub(re.escape(RENVOI), '', corps)
manquants = set()
corps = traduire_corps(corps, manquants)

# lien de langue : vers le français
corps = corps.replace(
    '<a class="langue" href="/en/" hreflang="en" lang="en" aria-label="Read this page in English" title="English">',
    '<a class="langue" href="/" hreflang="fr" lang="fr" aria-label="Lire cette page en français" title="Français">')
# ancres internes : rester sur la page anglaise
corps = corps.replace('href="/#', 'href="#')

tete = tete.replace('<html lang="fr">', '<html lang="en">', 1)
tete = re.sub(r'<title>.*?</title>', '<title>' + html.escape(TITRE_EN, quote=False) + '</title>', tete, count=1)
tete = meta(tete, 'name="description"', META['description'])
tete = meta(tete, 'property="og:title"', META['og_titre'])
tete = meta(tete, 'property="og:description"', META['og_description'])
tete = meta(tete, 'name="twitter:title"', META['og_titre'])
tete = meta(tete, 'name="twitter:description"', META['og_description'])
tete = meta(tete, 'property="og:url"', SITE + '/en/')
tete = re.sub(r'<meta property="og:locale" content="fr_FR">',
              '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="fr_FR">', tete)
alt = re.search(r'<meta property="og:image:alt" content="([^"]*)"', tete)
if alt and clef(html.unescape(alt.group(1))) in EN:
    tete = meta(tete, 'property="og:image:alt"', EN[clef(html.unescape(alt.group(1)))])
tete = tete.replace('<link rel="canonical" href="https://lapetitevague85.com/">',
                    '<link rel="canonical" href="https://lapetitevague85.com/en/">')
tete = tete.replace('<meta charset="utf-8">',
                    '<meta charset="utf-8">\n<script>window.LPV_LANGUE = \'en\';</script>', 1)

en = tete + corps
en = en.replace('<html lang="en">', '<html lang="en">\n<!-- Page produite par _traduction/gen.py à partir de index.html : ne pas modifier à la main. -->', 1)
os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
open(SORTIE, 'w', encoding='utf-8').write(en)

print('en/index.html écrite :', round(len(en) / 1024), 'Ko,', len(EN), 'phrases au dictionnaire')
if manquants:
    print(len(manquants), 'phrase(s) française(s) sans traduction :')
    for k in sorted(manquants):
        print('  -', k)
