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

- `[LIEN-AIRBNB]` — **deux fois** (bouton de la section 04 et pied de page) : collez l’URL
  de votre annonce Airbnb à la place, en gardant les guillemets.
- `[X]` voyageurs, `[X]` chambres, minutes jusqu’à la corniche et jusqu’aux commerces.
- `[Terrasse…]`, `[Stationnement…]`, `[Animaux…]` dans les équipements.
- `[@lapetitevague]` et le numéro de meublé de tourisme `[00000]`.

## Coordonnées affichées

223 bis rue Georges Clemenceau, 85270 Saint-Hilaire-de-Riez — **46.7046, -1.9509**
(géocodage de l’adresse ; pour une précision à la porte près, faites un appui long sur la maison
dans Google Maps, copiez les coordonnées et remplacez les deux occurrences dans `index.html`).

## Les photos

| Fichier | Où il apparaît |
|---|---|
| `photos/chambre.jpg` | Accroche |
| `photos/sejour.jpg` | Galerie, grande image |
| `photos/detail-chambre.jpg` | Galerie, détail |
| `photos/salle-eau.jpg` | Galerie |
| `photos/facade.jpg` | Bandeau pleine largeur |
| `photos/carte-quartier.jpg` | Section « Le lieu » |
| `photos/carte-cote.jpg` | Bandeau pleine largeur, bas de page |

Pour remplacer une photo : gardez le même nom de fichier, largeur ~1600 px, format JPEG.

Les deux vues aériennes sont des captures Google : la mention « © Google » est affichée sous
chacune et dans le pied de page, comme l’exigent les conditions d’utilisation. Si vous préférez
vous en passer, un fond OpenStreetMap (via `openstreetmap.org` → *Partager* → iframe) est libre d’usage.

## À refaire au prochain passage

- **La cuisine** : outils, bouteilles et reflet dans la vitre — pièce absente du site pour l’instant.
- **La deuxième chambre** : dressing à terminer, matelas encore sous plastique, volet fermé.
- **La terrasse / l’extérieur** : il manque une vue large et lumineuse.
- Conseils : lumière du matin ou de fin de journée, volets ouverts, appareil à hauteur de poitrine,
  depuis un angle de la pièce, **sans le mode panoramique** (il courbe les murs et les plinthes).
