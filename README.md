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
- Le prix d’appel « à partir de `[000] €` » dans la section Réserver. Un site qui cache son prix
  perd la moitié de ses visiteurs ; un ordre de grandeur suffit.
- L’avis de voyageur du bandeau sombre (deux lignes copiées d’Airbnb) et son prénom.
- La **cabine** : ce qu’elle contient exactement, et si elle ajoute un couchage.

**Important**

- Infos pratiques : arrivée, départ, durée minimum, remise des clés, ménage, taxe de séjour,
  animaux, stationnement.
- Équipements : terrasse, stationnement, abri vélos, congélateur, type de cafetière.
- Distances jusqu’aux deux gares.
- La question « convient-il à une famille ? » dans la FAQ.
- `[@lapetitevague]` et le numéro de meublé de tourisme `[00000]`.

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

## Les photos

| Fichier | Où il apparaît |
|---|---|
| `photos/chambre.jpg` | Accroche |
| `photos/sejour.jpg` | Galerie, grande image |
| `photos/detail-chambre.jpg` | Galerie, « Le coin du lit » |
| `photos/salle-eau.jpg` | Galerie |
| `photos/facade.jpg` | Bandeau pleine largeur |
| `photos/carte-quartier.jpg` | Section « Le lieu » |
| `photos/carte-cote.jpg` | Bandeau pleine largeur, bas de page |

Pour remplacer une photo : gardez le même nom de fichier, largeur ~1600 px, format JPEG.

Les deux vues aériennes sont des captures Google : la mention « © Google » est affichée sous
chacune et dans le pied de page, comme l’exigent les conditions d’utilisation. Si vous préférez
vous en passer, un fond OpenStreetMap (via `openstreetmap.org` → *Partager* → iframe) est libre d’usage.

## Structure de la page

Accroche · chiffres clés · 01 La maison (galerie + couchages) · Une journée ici · avis ·
02 Le lieu (distances, adresse, carte) · 03 L’environnement (les deux communes + l’île d’Yeu) ·
04 Les saisons · 05 Les équipements · 06 Infos pratiques (+ comment venir) ·
07 Questions fréquentes · 08 Réserver · pied de page.

Sur mobile, une barre de réservation apparaît dès qu’on a dépassé l’accroche et s’efface
en arrivant sur la section Réserver.

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
- **La terrasse / l’extérieur** : il manque une vue large et lumineuse — elle ferait une bien
  meilleure photo d’accroche que la chambre.
- Conseils : lumière du matin ou de fin de journée, volets ouverts, appareil à hauteur de poitrine,
  depuis un angle de la pièce, **sans le mode panoramique** (il courbe les murs et les plinthes).
