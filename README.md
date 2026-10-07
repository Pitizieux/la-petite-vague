# La petite vague

Site vitrine d’une maison de 55 m² en location saisonnière, entre mer et marais,
223 bis rue Georges Clemenceau — 85270 Saint-Hilaire-de-Riez.
Une seule page, sans dépendance ni outil de build : `index.html` + le dossier `photos/`.
Français et anglais, au choix du visiteur.

## L’adresse du site

**https://lapetitevague85.com** — nom de domaine déposé, servi par GitHub Pages.

Le fichier `CNAME` à la racine du dépôt porte le domaine : **ne le supprimez pas**, GitHub
Pages s’en sert pour accepter l’adresse. Côté registrar, la zone DNS doit contenir :

| Type | Nom | Valeur |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | pitizieux.github.io. |

Puis, sur GitHub : **Settings → Pages → Custom domain** → `lapetitevague85.com` → *Save*,
et cochez **Enforce HTTPS** une fois que la case devient disponible (elle attend que le
certificat soit émis, en général moins d’une heure après la propagation DNS).

Les quatre adresses A sont celles de GitHub Pages pour un domaine racine ; elles sont
communes à tous les sites hébergés là, c’est normal.

## Variante : héberger chez Hostinger plutôt que sur GitHub Pages

Possible seulement avec un **plan d’hébergement** Hostinger — le nom de domaine seul ne
suffit pas. Dans hPanel, si **Sites web** ne liste rien, il n’y a pas de plan.

Dans ce cas on ne touche pas au DNS : le domaine pointe déjà sur l’hébergement.
Le fichier `CNAME` et les enregistrements A de GitHub ne servent plus à rien.

1. **Le certificat d’abord.** hPanel → *Sites web* → **Gérer** → **SSL** → installez le
   certificat gratuit pour `lapetitevague85.com`. À faire **avant** de téléverser : le
   `.htaccess` force le HTTPS, et sans certificat les visiteurs tombent sur un
   avertissement de sécurité.
2. **Gestionnaire de fichiers** (même menu *Gérer*) → ouvrez `public_html` → supprimez ce
   qui s’y trouve (page de bienvenue, `default.php`). **Gardez** le dossier `.well-known`
   s’il existe : il sert à la validation du certificat.
3. Téléversez l’archive du site **dans `public_html`**, clic droit dessus → **Extraire**.
   Dans la fenêtre, la destination doit être `public_html` lui-même : laissez le nom de
   dossier vide, sinon tout atterrit dans un sous-dossier et le site reste introuvable.
   Supprimez l’archive une fois extraite.
4. **Vérifiez que `.htaccess` est bien là.** Il commence par un point, et les gestionnaires
   de fichiers masquent souvent ces fichiers : cherchez l’option « afficher les fichiers
   cachés ». S’il manque, créez-le et collez le contenu de `.htaccess` de ce dépôt.
5. Ouvrez `https://lapetitevague85.com`, puis `/robots.txt` et `/sitemap.xml` pour vérifier
   qu’ils répondent.

**Pour modifier le site ensuite** : faites la modification ici, poussez sur GitHub pour
garder l’historique, puis re-téléversez le ou les fichiers changés dans `public_html`
(`index.html` seul la plupart du temps — les photos ne bougent pas). Le `.htaccess` met la
page en cache une heure : forcez le rafraîchissement (Ctrl+F5) pour voir le résultat.

**À savoir** : les adresses e-mail sur le domaine (`contact@lapetitevague85.com`) dépendent
des enregistrements MX, pas de l’endroit où le site est hébergé. Vous pouvez donc garder la
messagerie Hostinger **et** le site sur GitHub Pages.

## Publier une modification

Le dépôt est `github.com/Pitizieux/la-petite-vague`, branche `main`, dossier racine.
GitHub Pages republie tout seul à chaque envoi, une à deux minutes après.

```bash
cd la-petite-vague
git add .
git commit -m "Ce que vous avez changé"
git push
```

Par l’interface, sans ligne de commande : ouvrez le fichier sur github.com, le crayon en
haut à droite, modifiez, puis *Commit changes*.

## À compléter dans `index.html`

Tout ce qui reste à remplir est **visible sur la page** : fond terracotta pâle et soulignement
pointillé. Cherchez `class="ac"` dans le fichier, ou `[` dans le texte.

Le site étant **déjà en ligne**, ces repères sont publics : à combler vite.

**1. Bloquant — on ne peut pas réserver**

- `[LIEN-AIRBNB]` — **trois fois** (lignes du bouton Réserver, du pied de page et de la barre
  mobile). C’est le seul repère **invisible** sur la page, puisque c’est une adresse :
  cherchez-le dans le fichier. Collez l’URL de l’annonce, en gardant les guillemets.

**2. Ce qu’un voyageur veut savoir avant de réserver**

- **Ménage** : `[110 €]` et `[Préciser : forfait par séjour ou par semaine.]` — le montant
  apparaît **deux fois**, dans Tarifs et dans Infos pratiques.
- **Taxe de séjour** : `[00 €]`, par personne et par nuit — **deux fois** également.
- **Horaires** : `[16 h]` à l’arrivée, `[10 h]` au départ, à valider avec Halo Conciergerie.
- **Numéro de déclaration en mairie** : `[00000]`, dans le pied de page. Obligation légale
  pour un meublé de tourisme, et exigé par l’office de tourisme pour vous référencer.

**3. Détails d’équipement**

- `[X]` places à table dans le séjour · `[avec congélateur ?]` · `[type]` de cafetière
- `[Salon de jardin, parasol, barbecue ?]`

**3. Le bandeau d’avis, mis en commentaire**

Le bandeau sombre qui citait un avis de voyageur est **masqué** dans le code (cherchez
`BANDEAU AVIS`). Il attend un avis réel : deux lignes copiées d’Airbnb, un prénom, un mois.
Retirez les deux lignes de commentaire pour le faire réapparaître.

Il n’y a pas d’avis inventé sur ce site, et il ne faut pas en mettre : un faux témoignage
présenté comme authentique est une pratique commerciale trompeuse, et les voyageurs
recoupent systématiquement avec les avis Airbnb.

**Un point à vérifier**

Le site annonce l’embarcadère de l’île d’Yeu **à 10 minutes à pied** et le port de
Saint-Gilles **à 20 minutes à pied** — ce sont les deux durées que vous aviez données.
Les deux sont cohérentes si l’embarcadère est de votre côté du chenal et le centre du port
de l’autre, après le pont ; c’est d’ailleurs ce que raconte la section « Une journée ici »
(« on remonte par le pont »). Un aller-retour à pied suffit à trancher : si les deux durées
sont proches, mieux vaut corriger, un voyageur qui compte sur dix minutes avec un bateau
à prendre ne pardonne pas l’écart.

Une fois une information remplie, retirez le `<span class="ac">…</span>` autour : le repère
coloré disparaît. Et pensez au dictionnaire anglais (`_traduction/en.py`) si le texte que
vous modifiez y a une clé — sinon il restera en français côté anglais.

**Photos qui manquent** : le bureau (une section entière lui est consacrée, sans photo) et
le mobilier d’extérieur (la terrasse et le jardin sont beaux mais vides — un voyageur peut
croire qu’il n’y a rien dehors).

## Coordonnées affichées

223 bis rue Georges Clemenceau, 85270 Saint-Hilaire-de-Riez — **46.7046, -1.9509**
(géocodage de l’adresse ; pour une précision à la porte près, faites un appui long sur la maison
dans Google Maps, copiez les coordonnées et remplacez les deux occurrences dans `index.html`).

## Le chapitre « Environnement »

Les activités des deux communes (corniche, bourrine du Bois Juquaud, marais salants, criée,
marchés) viennent du site de l'Office de tourisme du Pays de Saint-Gilles-Croix-de-Vie ;
le bloc « L'île d'Yeu, à la journée » vient de celui de l'île d'Yeu (ile-yeu.fr) et la durée
de traversée (1 h) de la Compagnie Vendéenne. Relevé le 4 octobre 2026. Le contenu est **écrit en dur** dans la page : il ne se met pas à jour
tout seul. Chaque entrée renvoie vers la page correspondante de l'office de tourisme, qui, elle,
reste à jour pour les horaires et les tarifs.

Les jours de marché sont à revérifier avant chaque saison (ils changent entre l'été et l'hiver).

## La conciergerie

L’accueil sur place et le suivi du séjour sont assurés par **Halo Conciergerie**
(Saint-Gilles-Croix-de-Vie), citée dans les infos pratiques, la FAQ et la section Réserver,
avec un lien vers [haloconcierge.fr](https://www.haloconcierge.fr/).

La liste des prestations complémentaires est rédigée à partir de leur site. Faites-la valider
par la conciergerie avant d’ouvrir le site au public, et ajustez-la à ce que vous avez
réellement convenu avec elle.

## Les photos

| Fichier | Où il apparaît |
|---|---|
| `photos/chambre.jpg` | Accroche |
| `photos/sejour.jpg` | Galerie « La maison » |
| `photos/cuisine.jpg` | Galerie « La maison » |
| `photos/terrasse.jpg` | Galerie « La maison » |
| `photos/facade.jpg` | Bandeau pleine largeur |
| `photos/carte-quartier.jpg` | Section « Le lieu » |
| `photos/carte-cote.jpg` | Bandeau pleine largeur |
| `photos/pf-*.jpg` | Portfolio « En images », onze photos |
| `photos/partage.jpg` | Nulle part sur la page : c’est la vignette d’aperçu du lien (1200 × 630, recadrée dans `pf-sejour-soir.jpg`) |

Pour remplacer une photo : gardez le même nom de fichier, largeur ~1600 px, format JPEG.

Les deux vues aériennes sont des captures Google : la mention « © Google » est affichée sous
chacune et dans le pied de page, comme l’exigent les conditions d’utilisation. Si vous préférez
vous en passer, un fond OpenStreetMap (via `openstreetmap.org` → *Partager* → iframe) est libre d’usage.

## Structure de la page

Accroche · chiffres clés · 01 La maison (galerie + couchages) · Une journée ici · avis ·
02 Le lieu (distances, adresse, carte) · 03 L’environnement (les deux communes + l’île d’Yeu) ·
04 Les saisons · 05 Les équipements · 06 Infos pratiques (+ la conciergerie, comment venir) ·
07 Questions fréquentes · 08 Réserver · pied de page.

Sur mobile, une barre de réservation apparaît dès qu’on a dépassé l’accroche et s’efface
en arrivant sur la section Réserver.

## Le plan

Le plan du rez-de-chaussée est un **SVG dessiné dans le code, au crayon et murs seuls**,
inline dans `index.html` (section « La maison »). Il est régénéré par `_plan/gen.py` :
modifiez le script, relancez-le, et recollez le contenu de `_plan/plan.svg` à la place
du `<svg>` existant.

Le rendu crayon vient de trois choses : chaque trait est tracé par `main_levee()`, qui
ajoute un tremblement lissé et un dépassement aux extrémités, puis repassé une seconde
fois en plus clair ; les murs sont pochés par des hachures à 45° générées mur par mur et
découpées sur un masque `evenodd` ; un filtre `feTurbulence` + `feDisplacementMap` donne
le grain du graphite. Les étiquettes sont en **Architects Daughter** (Google Fonts),
ajoutée au chargement des polices de la page.

Pour changer le rendu : `PAS_H` règle la densité des hachures, `amp` et `over` dans
`trait()` l’amplitude du tremblement et le dépassement, `scale` du filtre `grain` la
granulation.

Géométrie relevée sur le plan Kozikaza du 12/01/2025 (`Rez-de-chaussée 1/50`), qui est une
image : les murs ont été mesurés au pixel puis recalés sur les cotes imprimées
(450 et 313 pour la chambre, 900 et 788 pour l’emprise). Les surfaces affichées sont
celles du plan source.

**Un écart assumé** : le plan source nomme la petite pièce « Chambre 3,7 m² ». Elle est
nommée **Bureau** sur le site, conformément à l’usage réel et à l’annonce Airbnb.
De même, « Salle de bain » devient « Salle d’eau » : il y a une douche, pas de baignoire.

Sur mobile, le plan défile horizontalement (`min-width: 540px`) pour rester lisible.

## Le traitement des photos

Toutes les photos reçoivent le même étalonnage, appliqué à la production (pas en CSS) :
noirs levés pour un rendu mat, contraste adouci, légère chaleur, saturation retenue.
Le portfolio le reçoit à pleine force (0,85), les autres photos à force réduite (0,45),
de sorte que la section « En images » se détache sans jurer avec le reste.

Les deux captures cartographiques ne sont pas étalonnées.

Pour refaire une série, reprenez la fonction `doux()` du script de production, ou demandez
à Claude de régénérer les photos avec une autre force.

## Accessibilité et navigation

Audit WCAG 2.1 AA passé avec le plugin **Design** d’Anthropic, puis corrections :

- **Anneau de focus** terracotta de 3 px, visible au clavier uniquement (`:focus-visible`),
  en écume sur les fonds sombres. Avant, seul l’anneau par défaut du navigateur existait.
- **Lien d’évitement** « Aller au contenu » en premier élément tabulable, et repère `<main>`.
- **Visionneuse au clavier** : chaque photo est un bouton (`role="button"`, `tabindex="0"`),
  s’ouvre à Entrée ou Espace, se parcourt aux flèches, se ferme à Échap. Le focus reste
  piégé dans la visionneuse et revient sur la photo d’origine à la fermeture. La légende
  annonce la position (« 5 sur 18 »).
- **Sommaire mobile** : sous 1000 px, la navigation était simplement masquée sur une page
  de 20 000 px. Une barre haute apparaît en remontant et ouvre un sommaire plein écran.
- **Contrastes** relevés au-dessus de 4,5:1 : `--gris-clair` passe de `#5A6A68` à `#4E5D5A`,
  les crédits de `#8D8272` à `#766B5E`, les légendes à `#6B6052`.
- **Cibles tactiles** portées à 44 px de haut minimum (navigation, liens office de tourisme,
  adresse, pied de page, questions de la FAQ).
- `scroll-padding-top` de 72 px sur mobile, pour que les ancres ne passent pas sous la barre.

- **Contraste élevé de Windows** (`forced-colors`) : les boutons et les barres reçoivent un
  contour pour rester repérables quand le système impose ses couleurs ; le plan au crayon
  et le trait de vague gardent leur dessin, qui deviendrait illisible autrement.

Vérifié sans débordement horizontal à 1600, 1280, 1024, 768, 390, 360 et 320 px,
au zoom 200 %, et sans erreur JavaScript.

## La version anglaise

Un petit drapeau en haut à droite fait basculer toute la page en anglais : l’en-tête sur
ordinateur, la barre haute sur mobile, et la tête du sommaire plein écran. Il affiche la
langue **vers laquelle** on va — Union Jack et « EN » quand la page est en français,
tricolore et « FR » quand elle est en anglais.

Ce qui bascule : tous les textes, les descriptions des photos (lues par les lecteurs
d’écran), les libellés du plan, le titre de l’onglet, la description pour les moteurs de
recherche et l’aperçu du lien. Le `lang` de la page change aussi, pour que les synthèses
vocales prononcent correctement.

Trois choses se décident toutes seules :

- **au premier passage**, un navigateur qui n’est pas en français ouvre la page en anglais ;
- **le choix est retenu** d’une visite à l’autre ;
- **l’adresse suit** : passer en anglais ajoute `?lang=en`, ce qui rend la version anglaise
  partageable telle quelle. Elle n’est volontairement **pas** annoncée aux moteurs
  (pas de `hreflang`) : la traduction se fait dans le navigateur, Google ne voit que le
  français, et `?lang=en` passerait pour un doublon.

### Comment elle est faite

Le français reste écrit en dur dans `index.html`. L’anglais vit dans un dictionnaire, où
**chaque clé est la phrase française exacte** — à une exception près : les espaces
insécables et fines du texte s’écrivent dans les clés comme des **espaces ordinaires**,
parce que la comparaison normalise tous les blancs. Écrire `125 €` avec une insécable dans
une clé la rend introuvable, et la phrase reste en français. Au clic, un script parcourt la page, remplace
les textes reconnus et garde les originaux pour pouvoir revenir en arrière. Il n’y a donc
qu’une seule page à maintenir, pas deux.

Le dictionnaire est dans `_traduction/en.py`. Pour le modifier :

```bash
cd _traduction
python3 gen.py      # réécrit le bloc TRADUCTION:DEBUT…FIN dans index.html
```

**Le piège à connaître** : si vous changez une phrase française dans `index.html` sans
changer la clé correspondante dans `en.py`, cette phrase restera en français en version
anglaise. Pour vérifier, ouvrez la page **en français**, puis la console du navigateur
(F12 → Console) et tapez :

```js
LPV_ORPHELINS()
```

La fonction liste les textes que le dictionnaire ne connaît pas. En temps normal elle ne
renvoie que la marque, l’adresse, les noms propres et les repères `[…]` — tout le reste doit
avoir sa traduction.

L’anglais est britannique (*metres*, *centimetres*, *neighbourhood*), les prix passent devant
le nombre (75 € → €75), les décimales prennent un point (3,7 m² → 3.7 m²) et il n’y a pas
d’espace avant `%` `?` `!` `:`.

## Typographie française

Les espaces fines et insécables sont **dans le texte**, pas en CSS, pour qu’elles survivent
à un copier-coller :

- `U+00A0` (espace insécable) avant `:` et devant `€` — 61 occurrences ;
- `U+202F` (espace fine insécable) avant `? ! ;` et `%`, à l’intérieur des guillemets
  `« »`, et entre un nombre et son unité — 18 occurrences ;
- `U+2011` (trait d’union insécable) dans les mots courts qui se coupaient en fin de ligne :
  `week‑end`, `juillet‑août`, `plain‑pied`, `après‑midi`, `aller‑retour`, `demi‑journée`.
  Les noms de lieux longs (Saint‑Gilles‑Croix‑de‑Vie) restent sécables **à dessein** :
  insécables, ils débordaient de l’écran à 320 px.

Si vous retouchez un texte, ces caractères sont invisibles dans un éditeur. Le plus simple
est de copier une phrase voisine et de la modifier, plutôt que de retaper la ponctuation.

Ajouté aussi : `text-wrap: pretty` sur les paragraphes (plus de mot seul en fin de
paragraphe), `text-wrap: balance` sur les intertitres, et une couleur de sélection
aux teintes du site.

## L’impression

La page a une feuille de style d’impression : `Ctrl/Cmd + P` donne une fiche propre d’une
quinzaine de pages, utilisable comme livret d’accueil ou comme document à envoyer.

Ce qui change à l’impression : la navigation, les photos, le portfolio, la citation et la
section « Une journée ici » disparaissent ; les deux bandeaux sombres repassent en noir sur
blanc ; les grilles à deux colonnes se mettent sur une seule ; **les questions fréquentes
s’impriment dépliées** (un script les ouvre sur `beforeprint` et les referme après) ;
l’adresse de chaque lien est imprimée entre parenthèses, en minuscules. Le plan au crayon
s’imprime, lui, tel quel.

Les repères `[…]` restent visibles sur le papier : c’est volontaire, ils servent de
liste de relecture.

## Référencement et partage du lien

- **JSON-LD `VacationRental`** dans le `<head>` : adresse, coordonnées, surface, capacité,
  équipements. À compléter avec l’URL de l’annonce quand le lien Airbnb sera connu.
- **Aperçu du lien** (Open Graph + carte Twitter) : quand vous envoyez l’adresse du site par
  SMS, WhatsApp, Messenger ou mail, le destinataire voit une vignette avec le séjour du soir,
  le titre et une phrase. L’image dédiée est `photos/partage.jpg`, au format 1200 × 630
  attendu par ces applications.
- Favicon et icône d’écran d’accueil en SVG inline (le trait de vague), titre raccourci
  à 58 caractères.
- `fetchpriority="high"` sur la photo d’accroche, `loading="lazy"` et dimensions sur toutes
  les autres, `decoding="async"` partout.

- `robots.txt` et `sitemap.xml` à la racine, pour que Google trouve la page.
- Titre de 60 caractères et description de 155 : au-delà, Google coupe.

**Si le site change d’adresse** (nom de domaine à vous, autre hébergeur), huit adresses
absolues sont à mettre à jour : six dans le `<head>` d’`index.html`, signalées par un
commentaire juste au-dessus — `canonical`, `og:url`, `og:image`,
`twitter:image`, puis `url` et `image` dans le bloc JSON-LD — plus `robots.txt` et
l’adresse de `sitemap.xml`. Une adresse relative ne produit **aucun** aperçu de lien :
c’est la raison pour laquelle elles sont écrites en entier.

Après une mise en ligne, Facebook et LinkedIn gardent l’ancien aperçu en cache pendant
quelques jours. Leurs outils de débogage respectifs permettent de forcer une relecture.

## Poids de la page

Mesuré, pas estimé : 63 Ko de HTML compressé (GitHub Pages sert le gzip), et 822 Ko de
photos au premier écran. Les images sont déjà encodées au bon point — les ré-encoder plus
fort ne gagne que 13 % en dégradant visiblement. Rien à optimiser ici.

Si vous remplacez une photo, visez 1400 à 1600 px de large et une qualité JPEG autour de 85 :
c’est le réglage du reste de la série.

## Les animations

Discrètes et sans bibliothèque : l’accroche monte à l’ouverture, le trait du logo se dessine,
les blocs apparaissent au défilement (en cascade pour les listes), les photos se rapprochent
légèrement au survol, le motif de vagues dérive, la FAQ s’ouvre en douceur.

Deux garde-fous :

- **Sans JavaScript**, la classe `anim` n’est jamais posée et la page s’affiche entièrement —
  rien ne reste caché.
- Le réglage **« réduire les animations »** du système (macOS, Windows, iOS, Android) coupe
  tout, y compris la dérive des vagues.

Pour tout désactiver : supprimez le petit script en fin de `<head>`.

## À refaire au prochain passage

- **La cuisine** : outils, bouteilles et reflet dans la vitre — pièce absente du site pour l’instant.
- **La deuxième chambre / la cabine** : dressing à terminer, matelas sous plastique, volet fermé.
  C’est la photo qui manque le plus : on vend « 1 chambre + cabine » sans montrer la cabine.
- **Le bureau** : une section entière lui est consacrée, toujours sans photo. Le bureau face
  à la fenêtre, volet ouvert, un ordinateur et une tasse posés dessus.
- **Le mobilier d’extérieur** : les photos de terrasse et de jardin sont belles mais vides.
  Une table, deux chaises et le voile d’ombrage déployé, en fin de journée : c’est ce qui
  fait qu’on se projette. En l’état, un voyageur peut croire qu’il n’y a rien dehors.
- Conseils : lumière du matin ou de fin de journée, volets ouverts, appareil à hauteur de poitrine,
  depuis un angle de la pièce, **sans le mode panoramique** (il courbe les murs et les plinthes).
