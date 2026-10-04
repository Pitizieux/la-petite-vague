# La petite vague

Site vitrine d’une maison de 55 m² en location saisonnière, entre mer et marais,
223 bis rue Georges Clemenceau — 85270 Saint-Hilaire-de-Riez.
Une seule page, sans dépendance ni outil de build : `index.html` + le dossier `photos/`.

## Mettre en ligne sur GitHub Pages

1. github.com → **New repository** → nom `la-petite-vague` → **Public** → *Create repository*.
2. Sur la page du dépôt vide : **uploading an existing file**, glissez `index.html`, `README.md`
   et le dossier `photos/`. *Commit changes*.
3. **Settings → Pages** → *Source* : `Deploy from a branch` → branche `main`, dossier `/ (root)` → *Save*.
4. Une à deux minutes plus tard : `https://VOTRE-PSEUDO.github.io/la-petite-vague/`.

En ligne de commande :

```bash
cd la-petite-vague
git init -b main
git add .
git commit -m "Site La petite vague"
git remote add origin https://github.com/VOTRE-PSEUDO/la-petite-vague.git
git push -u origin main
```

## À compléter dans `index.html`

Tout ce qui reste à remplir est **visible sur la page** : fond terracotta pâle et soulignement
pointillé. Cherchez `class="ac"` dans le fichier, ou `[` dans le texte.

**Indispensable avant d’ouvrir le site au public**

- `[LIEN-AIRBNB]` — **trois fois** : bouton de la section Réserver, pied de page, barre mobile.
  Collez l’URL de l’annonce à la place, en gardant les guillemets.
- L’avis de voyageur du bandeau sombre (deux lignes copiées d’Airbnb) et son prénom.
- **Ménage** : 110 € est affiché, mais il reste à préciser si c’est un forfait par séjour ou
  par semaine. La section Tarifs et les infos pratiques portent le même repère.
- **Taxe de séjour** : montant par personne et par nuit.

**Important**

- Places à table dans le séjour, type de cafetière, congélateur.
- Salon de jardin, parasol, barbecue sur la terrasse.
- `[@lapetitevague]` et le numéro de déclaration en mairie (`[00000]`).
- Horaires d’arrivée et de départ, à valider avec Halo Conciergerie.

Une fois une information remplie, retirez le `<span class="ac">…</span>` autour : le repère
coloré disparaît.

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
