# -*- coding: utf-8 -*-
"""Traduction anglaise de La petite vague.

Chaque clé est le texte français EXACT tel qu'il apparaît dans index.html
(espaces multiples réduites à une, bords rognés). Le script gen.py
transforme ce dictionnaire en bloc JavaScript inséré dans la page.

Anglais britannique : metres, centimetres, neighbourhood.
Les prix passent devant le nombre (75 € → €75), les décimales prennent
un point (3,7 m² → 3.7 m²), et il n'y a pas d'espace avant % ? ! :
"""

EN = {

# ——— Navigation, en-tête, sommaire ———————————————————————————
"Aller au contenu": "Skip to content",
"Sommaire": "Contents",
"Fermer le sommaire": "Close the contents",
"Sommaire du site": "Site contents",
"Sections de la page": "Page sections",
"La maison": "The house",
"Le bureau": "The study",
"En images": "In pictures",
"Le lieu": "Where it is",
"L’environnement": "Around here",
"Les équipements": "What's included",
"Les tarifs": "Rates",
"Infos pratiques": "Good to know",
"Questions fréquentes": "Common questions",
"Réserver": "Book",
"Autour": "Around",
"Tarifs": "Rates",
"Pratique": "Practical",

# ——— Accroche ————————————————————————————————————————————————
"Saint-Hilaire-de-Riez · entre mer et marais": "Saint-Hilaire-de-Riez · between sea and marsh",
"Cinquante-cinq mètres carrés de calme, posés entre l’océan et les marais. Le matin, la lumière monte du marais ; le soir, la mer se retire derrière les dunes et l’on entend le vent passer dans les pins. Le temps d’un week‑end, ou de tout un été.":
  "Fifty-five square metres of quiet, set down between the ocean and the marshes. In the morning the light comes up off the water; in the evening the sea pulls back behind the dunes and you can hear the wind moving through the pines. For a weekend, or for a whole summer.",
"2 voyageurs": "2 guests",
"Terrasse et jardin privatifs": "Private terrace and garden",
"Corniche à 10 min à pied": "Clifftop path 10 min on foot",
"Voir les disponibilités": "See available dates",
"Découvrir la maison": "Look round the house",
"de plain‑pied": "all on one level",
"de terrasse et jardin": "of terrace and garden",
"voyageurs": "guests",
"à pied de la plage": "walk to the beach",

# ——— 01 La maison ————————————————————————————————————————————
"01 — La maison": "01 — The house",
"Petite, claire,": "Small, bright,",
"et pensée pour": "and built for",
"ralentir": "slowing down",
"Du bois clair, du lin, des murs couleur de vague et beaucoup de jour. Tout est de plain‑pied : une chambre, un bureau, une salle d’eau, un séjour ouvert sur la cuisine. Et, devant comme derrière, cent dix mètres carrés d’extérieurs rien qu’à vous.":
  "Pale wood, linen, walls the colour of a wave, and a great deal of daylight. Everything is on one level: a bedroom, a study, a shower room, a living room open onto the kitchen. And front and back, a hundred and ten square metres of outdoors that are yours alone.",
"Le lit est fait à votre arrivée, les serviettes pliées dessus. La cuisine est faite pour cuisiner vraiment — du poisson pris au port le matin, du sel de Vendée, une table que personne ne quitte avant la nuit.":
  "The bed is made when you arrive, the towels folded on top. The kitchen is meant for proper cooking — fish bought at the harbour that morning, Vendée salt, a table nobody leaves before dark.",
"Le séjour": "The living room",
"La cuisine": "The kitchen",
"La terrasse": "The terrace",
"La chambre": "The bedroom",
"Un lit double de 160 cm": "One double bed, 160 cm",
"Pièce à part, pour travailler au calme": "A room of its own, for working in peace",
"La salle d’eau": "The shower room",
"Douche, vasque, sèche-serviettes · WC séparés": "Shower, basin, heated towel rail · separate WC",
"Le séjour et la cuisine": "The living room and kitchen",
"Pièce de vie ouverte, table pour quatre": "Open living space, table for four",
"55 m² en façade, privatifs": "55 m² at the front, private",
"Le jardin": "The garden",
"55 m² engazonnés à l’arrière, privatifs": "55 m² of lawn at the back, private",

# ——— Le plan au crayon ———————————————————————————————————————
"Bureau": "Study",
"Salle d’eau": "Shower room",
"Chambre": "Bedroom",
"Séjour et cuisine": "Living room and kitchen",
"3,7 m²": "3.7 m²",
"3,1 m²": "3.1 m²",
"14,1 m²": "14.1 m²",
"31,8 m²": "31.8 m²",
"baie sur la terrasse": "sliding door to terrace",
"entrée": "entrance",
"rez-de-chaussée · cotes en centimètres": "ground floor · dimensions in centimetres",
"Plan": "Floor plan",
"Le rez-de-chaussée, de plain‑pied": "The ground floor, all on one level",
"Faites glisser le plan pour le parcourir en entier.": "Drag the plan sideways to see all of it.",
"Plan au crayon du rez-de-chaussée : chambre, bureau, salle d’eau, WC, séjour ouvert sur la cuisine, baie sur la terrasse":
  "Pencil plan of the ground floor: bedroom, study, shower room, WC, living room open onto the kitchen, sliding door to the terrace",

# ——— 02 Le bureau ————————————————————————————————————————————
"02 — Le bureau": "02 — The study",
"Télétravailler,": "Working from here,",
"la mer": "the sea",
"au bout de la rue": "at the end of the road",
"Ce n’est pas un coin de table ni un bout de chambre : c’est une pièce à part, avec sa porte, son bureau et sa fenêtre. On y passe la matinée au calme, et l’on referme à midi.":
  "Not a corner of the table, not a nook in the bedroom: a room of its own, with a door, a desk and a window. You spend the morning in it, and close the door at lunchtime.",
"Une pièce dédiée": "A room kept for it",
"Porte fermée, lumière du jour, et le reste de la maison qui ne bouge pas pendant que vous travaillez.":
  "A door that shuts, daylight, and the rest of the house staying put while you work.",
"Fibre et visios": "Fibre, and video calls",
"Wifi fibre, assez de débit pour enchaîner les visioconférences sans y penser.":
  "Fibre wifi, with enough headroom to run video calls back to back without thinking about it.",
"La pause à dix minutes": "A ten-minute break",
"La corniche à dix minutes de marche, la plage à quinze. De quoi couper vraiment entre deux réunions.":
  "The clifftop path is ten minutes away on foot, the beach fifteen. Enough to properly stop between two meetings.",
"Au mois, l’hiver": "By the month, in winter",
"Pour un séjour long hors saison, la nuitée baisse de 25 à 30 %. Une parenthèse de travail au bord de l’eau, à prix de novembre.":
  "For a long off-season stay the nightly rate drops by 25–30%. A stretch of work by the sea, at November prices.",

# ——— Une journée ici —————————————————————————————————————————
"Une journée ici": "A day here",
"Du café du matin": "From the first coffee",
"au": "to the",
"dernier bain": "last swim",
"Rien d’obligatoire, bien sûr. Mais voilà à quoi ressemble une journée quand on ne force rien.":
  "None of it compulsory, of course. But this is what a day looks like when nothing is forced.",
"8 h": "8 am",
"Le pain, puis le marais": "Bread first, then the marsh",
"Sept minutes de marche jusqu’à la boulangerie, et l’on revient par les chemins du marais : l’eau est plate, les hérons décollent sans bruit. Café sur la terrasse, le temps que la journée se décide.":
  "Seven minutes' walk to the bakery, then back along the marsh paths: the water flat, herons lifting off without a sound. Coffee on the terrace, while the day makes up its mind.",
", le temps que la journée se décide.": ", while the day makes up its mind.",
"Midi": "Midday",
"La corniche et la plage": "The clifftop path and the beach",
"Dix minutes à pied et l’on y est : les rochers bruns, le Trou du Diable qui crache l’écume les jours de houle. Puis la plage de Boisvinet, en pente douce, pour le bain et la sieste.":
  "Ten minutes on foot and you're there: brown rock, and the Trou du Diable throwing up spray on a swell. Then Boisvinet beach, shelving gently, for a swim and a doze.",
"18 h": "6 pm",
"Le retour des bateaux": "The boats come in",
"À Saint-Gilles, les sardiniers rentrent en fin d’après‑midi. On achète le poisson du jour, on remonte par le pont, et l’on cuisine en laissant la fenêtre ouverte sur le soir.":
  "Over in Saint-Gilles the sardine boats come in late in the afternoon. You buy the day's catch, walk back over the bridge, and cook with the window open on the evening.",
"[Un avis de voyageur, copié depuis Airbnb — deux lignes suffisent.]":
  "[A guest review, copied from Airbnb — two lines is plenty.]",
"[Prénom]": "[First name]",
"[mois année]": "[month year]",

# ——— 03 En images ————————————————————————————————————————————
"03 — En images": "03 — In pictures",
"Les petites choses": "The small things",
"qu’on": "you end up",
"remarque": "noticing",
"Six coquillages accrochés au mur, deux verres posés sur la table basse quand le soleil descend, le lit qui réapparaît dans le miroir rond. On ne les remarque pas tout de suite, et puis on ne voit plus qu’elles.":
  "Six shells hung on the wall, two glasses left on the coffee table as the sun drops, the bed reappearing in the round mirror. You don't notice them at first, and then you see nothing else.",
"Le bleu de la chambre": "The blue of the bedroom",
"Six coquillages, rien d’autre": "Six shells, nothing else",
"L’heure des deux verres": "The hour of two glasses",
"La terrasse, le matin": "The terrace, in the morning",
"La chambre, dans le miroir": "The bedroom, in the mirror",
"De l’autre côté": "The other side",
"Le rond du miroir": "The round of the mirror",
"Le soir entre par la baie": "Evening comes in through the glass",
"Tout en blanc": "All in white",
"Le jardin, derrière": "The garden, behind",
"La table du matin": "The morning table",
"Vu du ciel, du toit de la maison jusqu’à l’océan": "From the sky, from the roof up to the ocean",
"La rue, la plage, puis l’océan": "The street, the beach, then the ocean",
"La maison et son jardin, vus d’en haut": "The house and its garden, from above",
"Le quartier vu du ciel, la plage et l’océan au loin": "The neighbourhood from the air, with the beach and the ocean beyond",
"La maison et son jardin vus d’en haut, au coin de la rue": "The house and its garden from above, on the street corner",
"Survol en drone, de la maison jusqu’à l’océan": "Drone flight, from the house to the ocean",
"La maison — 223 bis rue Georges Clemenceau, Saint-Hilaire-de-Riez":
  "The house — 223 bis rue Georges Clemenceau, Saint-Hilaire-de-Riez",

# ——— 04 Le lieu ——————————————————————————————————————————————
"04 — Le lieu": "04 — Where it is",
"Entre la mer": "Between the sea",
"et le": "and the",
"marais": "marsh",
"D’un côté les dunes, la corniche et l’écume qui saute sur les rochers — dix minutes de marche, pas davantage. De l’autre, les marais : des chemins plats, des reflets immobiles et des oiseaux qui s’envolent au petit matin. La maison tient entre les deux, et tout se fait à pied.":
  "On one side the dunes, the clifftop path and the spray jumping off the rocks — ten minutes on foot, no more. On the other the marshes: flat paths, still reflections, birds lifting off at first light. The house sits between the two, and everything is walkable.",
"Commerces et boulangerie": "Shops and bakery",
"7 min à pied": "7 min walk",
"Corniche vendéenne": "The Corniche vendéenne",
"10 min à pied": "10 min walk",
"Embarcadère pour l’île d’Yeu": "Ferry pier for the Île d'Yeu",
"Plage de Boisvinet": "Boisvinet beach",
"15 min à pied": "15 min walk",
"Port de Saint-Gilles-Croix-de-Vie": "Saint-Gilles-Croix-de-Vie harbour",
"20 min à pied · 5 min en voiture": "20 min walk · 5 min drive",
"Gare de Saint-Hilaire-de-Riez": "Saint-Hilaire-de-Riez station",
"L’adresse": "The address",
"ouvrir dans Maps": "open in Maps",
"La maison, le port et la plage": "The house, the harbour and the beach",
"La côte, du marais breton à l’île d’Yeu": "The coast, from the Breton marsh to the Île d'Yeu",

# ——— 05 L’environnement ——————————————————————————————————————
"05 — L’environnement": "05 — Around here",
"Ce qu’il y a": "What's",
"tout": "all",
"autour": "around",
"Deux communes se partagent l’horizon : Saint-Hilaire-de-Riez côté dunes et marais, Saint-Gilles-Croix-de-Vie côté port. Voici ce qu’on va y voir le plus volontiers — l’office de tourisme tient le reste à jour.":
  "Two towns share the horizon: Saint-Hilaire-de-Riez on the dune and marsh side, Saint-Gilles-Croix-de-Vie on the harbour side. Here's what we go and see most often — the tourist office keeps the rest up to date.",
"La Corniche vendéenne": "The Corniche vendéenne",
"Trois kilomètres de rochers bruns entre Sion et Saint-Gilles, une heure de marche facile. Au Trou du Diable, les jours de houle, la mer remonte par la faille et retombe en écume blanche. Table d’orientation, coucher de soleil face à l’île d’Yeu.":
  "Three kilometres of brown rock between Sion and Saint-Gilles, an easy hour's walk. At the Trou du Diable, on a swell, the sea forces up through the fissure and falls back as white spray. A viewing table, and sunset facing the Île d'Yeu.",
"L’itinéraire à pied": "The walking route",
"La Bourrine du Bois Juquaud": "La Bourrine du Bois Juquaud",
"Une maison de marais basse et blanche, toit de roseaux, bâtie en 1818 et restée dans son jus. Une heure de visite pour comprendre comment on vivait dans le marais breton il y a un siècle. Parfait les jours de pluie.":
  "A low, white marsh cottage under a reed roof, built in 1818 and left exactly as it was. An hour's visit, and you understand how people lived in the Breton marsh a century ago. Perfect on a wet day.",
"Le musée": "The museum",
"Les marais salants": "The salt marshes",
"Quatre mille cinq cents hectares d’eau plate et de digues, où l’on récolte encore le sel à la main. Les sauniers ouvrent leurs œillets à la visite en saison ; on repart avec un sachet de fleur de sel.":
  "Four and a half thousand hectares of flat water and dykes, where the salt is still raked by hand. In season the salt workers open their pans to visitors; you leave with a bag of fleur de sel.",
"Visites et découvertes": "Visits and discoveries",
"Les plages et la base nautique": "The beaches and the watersports centre",
"Douze kilomètres de sable : les Demoiselles, les Salins, les Mouettes, la Grande Plage de Sion. À la base nautique des Demoiselles, on loue un kayak, une planche ou un dériveur à l’heure.":
  "Twelve kilometres of sand: les Demoiselles, les Salins, les Mouettes, the Grande Plage at Sion. At the Demoiselles centre you can hire a kayak, a board or a dinghy by the hour.",
"Activités nautiques": "Watersports",
"Le port de pêche et la criée": "The fishing harbour and the auction",
"Quatre mille tonnes de poisson bleu par an — sardine, anchois. En fin d’après‑midi, les bateaux rentrent et l’on peut suivre la vente à la criée depuis Escale Pêche, au cœur du port.":
  "Four thousand tonnes of oily fish a year — sardine, anchovy. Late in the afternoon the boats come in and you can watch the auction from Escale Pêche, in the middle of the harbour.",
"Escale Pêche": "Escale Pêche",
"Les marchés": "The markets",
"Mardi, jeudi et dimanche matin place Saint-Gilles ; mercredi et samedi matin place Sainte-Croix. Poisson du jour, légumes du marais, brioche vendéenne.":
  "Tuesday, Thursday and Sunday morning on place Saint-Gilles; Wednesday and Saturday morning on place Sainte-Croix. The day's fish, marsh vegetables, Vendée brioche.",
"L’agenda": "What's on",
"Le quartier du Maroc et la Petite Île": "The Maroc quarter and the Petite Île",
"Les ruelles basses bâties par les marins avec les pierres de lest rapportées du large, la Maison du Pêcheur, le pont de la Concorde et sa statue de marin qui sert de jauge aux crues.":
  "Low lanes the sailors built from ballast stone brought back from the fishing grounds, the Maison du Pêcheur, the pont de la Concorde and its sailor statue that doubles as a flood gauge.",
"À voir, à faire": "What to see and do",
"La Vélodyssée": "La Vélodyssée",
"La véloroute du littoral passe ici : pistes plates et abritées vers Saint-Jean-de-Monts au nord, Brétignolles au sud. De quoi faire une journée entière sans jamais quitter le bord de mer.":
  "The coastal cycle route runs through here: flat, sheltered tracks north to Saint-Jean-de-Monts, south to Brétignolles. Enough for a whole day without ever leaving the sea.",
"Activités outdoor": "Outdoor activities",

# ——— L’île d’Yeu —————————————————————————————————————————————
"L’île d’Yeu,": "The Île d'Yeu,",
"à la journée": "in a day",
"L’embarcadère est à dix minutes à pied : on part le matin, une heure de mer, et l’on rentre le soir avec du sel sur la peau. Vingt-trois kilomètres carrés de granit et de pins, à faire à vélo — c’est la bonne échelle.":
  "The pier is ten minutes away on foot: you leave in the morning, an hour at sea, and come back in the evening with salt on your skin. Twenty-three square kilometres of granite and pine, best done by bike — that's the right scale for it.",
"La traversée": "The crossing",
"Compagnie Vendéenne, embarcadère avenue Jean Cristau. Une heure de mer, aller‑retour dans la journée. Réservez à l’avance en été.":
  "Compagnie Vendéenne, pier on avenue Jean Cristau. An hour at sea, there and back in a day. Book ahead in summer.",
"Sur place": "Once you're there",
"Location de vélos à la descente du bateau, à Port-Joinville.": "Bike hire as you step off the boat, at Port-Joinville.",
"Deux côtes en une île": "Two coasts on one island",
"Au sud-ouest, la côte sauvage : les falaises, le port de la Meule au creux de son anse, les criques des Soux, des Fontaines, des Sabias en contrebas du Vieux Château. Au nord-est, le sable long et calme — Ker Châlon, les Sapins, les Conches, les Vieilles. Une trentaine de plages en tout, et l’on finit toujours par en trouver une déserte.":
  "To the south-west the wild coast: cliffs, the little harbour of La Meule tucked in its cove, the creeks of Les Soux, Les Fontaines and Les Sabias below the old castle. To the north-east, long quiet sand — Ker Châlon, Les Sapins, Les Conches, Les Vieilles. Thirty-odd beaches in all, and you always end up finding an empty one.",
"Le Vieux Château et les pierres levées": "The old castle and the standing stones",
"Une forteresse posée sur un îlot de rocher, bâtie entre le XIVᵉ et le XVIIᵉ siècle face au large. Ailleurs sur l’île, des dolmens et des menhirs de cinq mille ans, le Grand Phare, l’église Saint-Sauveur et les quais de Port-Joinville.":
  "A fortress set on a rock islet, built between the 14th and 17th centuries facing the open sea. Elsewhere on the island: dolmens and menhirs five thousand years old, the Grand Phare lighthouse, the church of Saint-Sauveur and the quays at Port-Joinville.",
"Soixante-douze kilomètres de chemins": "Seventy-two kilometres of paths",
"Balisés, plats, ouverts au vélo comme à la marche. On fait le tour par le sentier côtier, en s’arrêtant où bon semble.":
  "Waymarked, flat, open to bikes and walkers alike. You can go right round on the coast path, stopping wherever you feel like it.",
"Office de tourisme de l’île d’Yeu": "Île d'Yeu tourist office",
"Les horaires et les tarifs changent au fil des saisons :": "Opening times and prices change with the season:",
"l’Office de tourisme du Pays de Saint-Gilles-Croix-de-Vie": "the Pays de Saint-Gilles-Croix-de-Vie tourist office",
"tient tout cela à jour.": "keeps all of it up to date.",

# ——— Les saisons —————————————————————————————————————————————
"Les saisons": "The seasons",
"Quand": "When to",
"venir": "come",
"La maison ne se ferme pas l’hiver, et c’est peut-être là qu’elle est le plus elle-même.":
  "The house doesn't close for winter, and that may be when it is most itself.",
"Mars à juin": "March to June",
"La lumière revient": "The light comes back",
"Les plages sont à vous, les chemins du marais sentent le sel et l’herbe neuve. Les terrasses rouvrent sans la foule et l’eau se réchauffe doucement. La meilleure saison pour le vélo.":
  "The beaches are yours, the marsh paths smell of salt and new grass. The cafés put their tables out again without the crowds, and the water slowly warms. The best season for cycling.",
"Juillet et août": "July and August",
"Le plein été": "High summer",
"Les marchés débordent, les sardiniers rentrent chaque soir, les baignades durent jusqu’à vingt-deux heures. On réserve tôt — et l’on se lève tôt pour avoir la corniche pour soi.":
  "The markets overflow, the sardine boats come in every evening, and people are still swimming at ten at night. Book early — and get up early, to have the clifftop path to yourself.",
"Septembre et octobre": "September and October",
"L’arrière-saison": "The after-season",
"L’eau est encore bonne, la lumière devient dorée et tout redevient tranquille. Beaucoup la préfèrent à l’été, et l’on comprend pourquoi.":
  "The water is still good, the light turns golden and everything goes quiet again. Plenty of people prefer it to summer, and you can see why.",
"Novembre à février": "November to February",
"Les tempêtes": "The storms",
"Le chauffage, un pull, et la corniche sous le vent : c’est le moment où le Trou du Diable crache le plus haut. On rentre se faire un thé, et la maison fait le reste.":
  "The heating on, a jumper, and the clifftop path in the wind: this is when the Trou du Diable throws water highest. You come back in and make tea, and the house does the rest.",

# ——— 06 Les équipements ——————————————————————————————————————
"06 — Les équipements": "06 — What's included",
"Tout ce qu’il faut,": "Everything you need,",
"rien de": "nothing",
"plus": "more",
"Vous arrivez les mains vides : le linge est fourni, les lits sont faits, la cuisine est équipée pour de vrais repas.":
  "You arrive empty-handed: linen provided, the bed made, the kitchen equipped for real meals.",
"Four et plaques de cuisson": "Oven and hob",
"Lave-vaisselle": "Dishwasher",
"Réfrigérateur avec congélateur": "Fridge with freezer",
"Micro-ondes, bouilloire, cafetière Nespresso": "Microwave, kettle, Nespresso machine",
"Salon de jardin et barbecue": "Garden furniture and barbecue",
"Vaisselle et ustensiles pour deux": "Crockery and utensils for two",
"Le confort": "Comfort",
"Lit fait à l’arrivée, linge de toilette fourni": "Bed made on arrival, towels provided",
"Lave-linge": "Washing machine",
"Wifi fibre": "Fibre wifi",
"Télévision": "Television",
"Chauffage dans chaque pièce": "Heating in every room",
"Sèche-serviettes dans la salle d’eau": "Heated towel rail in the shower room",
"Dehors et accès": "Outside and access",
"Terrasse de 55 m² en façade, privative": "55 m² private terrace at the front",
"Jardin engazonné de 55 m² à l’arrière, privatif": "55 m² private lawn at the back",
"Stationnement gratuit dans la rue, places nombreuses": "Free parking in the street, plenty of space",
"Maison de plain‑pied, sans marche": "All on one level, no steps",
"Animaux non admis · logement non-fumeur": "No pets · non-smoking",

# ——— 07 Les tarifs ———————————————————————————————————————————
"07 — Les tarifs": "07 — Rates",
"Ce que coûte": "What a night",
"une": "here",
"nuit ici": "costs",
"Prix par nuit pour deux, hors ménage et taxe de séjour. Le second montant s’applique aux nuits du vendredi et du samedi.":
  "Per night for two, before cleaning and tourist tax. The second figure applies to Friday and Saturday nights.",
"Saison creuse": "Low season",
"Octobre, novembre, janvier à mars hors vacances": "October, November, January to March outside the holidays",
"75 € · 85 €": "€75 · €85",
"2 nuits minimum": "2 nights minimum",
"Vacances scolaires, juin et septembre": "School holidays, June and September",
"Toussaint, Noël, février, printemps — et les deux mois qui encadrent l’été":
  "All Saints', Christmas, February, Easter holidays — and the two months either side of summer",
"95 € · 105 €": "€95 · €105",
"2 nuits · 3 en vacances": "2 nights · 3 in the holidays",
"Ponts et week‑ends fériés": "Long weekends and bank holidays",
"Pâques, Ascension, Pentecôte": "Easter, Ascension, Whitsun",
"115 € à 120 €": "€115 to €120",
"3 nuits minimum": "3 nights minimum",
"Plein été": "High summer",
"120 € · 130 €": "€120 · €130",
"5 nuits en juillet · 7 en août": "5 nights in July · 7 in August",
"À la semaine": "By the week",
"— 10 % de moins hors juillet‑août.": "— 10% off outside July and August.",
"— 25 à 30 % de moins. C’est la formule pensée pour le télétravail, bureau compris.":
  "— 25–30% off. This is the one meant for working remotely, study included.",
"Ménage": "Cleaning",
"— forfait de 125 € en fin de séjour.": "— a flat €125 at the end of the stay.",
"Taxe de séjour": "Tourist tax",
"— collectée par Airbnb au moment de la réservation.": "— collected by Airbnb when you book.",
"Forfait de 125 €": "Flat fee of €125",
"Collectée par Airbnb": "Collected by Airbnb",
"Ces montants sont indicatifs : le calendrier d’Airbnb fait foi, et les prix y suivent la demande au jour le jour.":
  "These figures are a guide: the Airbnb calendar is what counts, and prices there follow demand day by day.",

# ——— 08 Infos pratiques ——————————————————————————————————————
"08 — Infos pratiques": "08 — Good to know",
"Les détails qui": "The details that",
"évitent les": "save you",
"questions": "asking",
"Tout est aussi rappelé dans le livret d’accueil, posé sur la table en arrivant.":
  "All of it is in the welcome book too, waiting on the table when you arrive.",
"Arrivée": "Check-in",
"À partir de": "From",
"[16 h]": "[4 pm]",
"Départ": "Check-out",
"Avant": "Before",
"[10 h]": "[10 am]",
"Durée minimum": "Minimum stay",
"2 à 7 nuits selon la saison": "2 to 7 nights depending on the season",
"Accueil et remise des clés": "Welcome and keys",
"Sur place, par Halo Conciergerie": "In person, by Halo Conciergerie",
"Ménage de fin de séjour": "End-of-stay cleaning",
"Animaux": "Pets",
"Non admis": "Not allowed",
"Stationnement": "Parking",
"Gratuit dans la rue": "Free in the street",

# ——— La conciergerie ——————————————————————————————————————————
"Qui vous accueille": "Who meets you",
"Halo Conciergerie,": "Halo Conciergerie,",
"à": "in",
"Saint-Gilles": "Saint-Gilles",
"Une conciergerie professionnelle installée à Saint-Gilles-Croix-de-Vie vous reçoit à votre arrivée, vous remet les clés et vous montre la maison. Elle reste joignable pendant tout le séjour : une question, un imprévu, une envie de dernière minute, c’est à elle qu’on s’adresse.":
  "A professional concierge service based in Saint-Gilles-Croix-de-Vie meets you on arrival, hands over the keys and shows you round. They stay reachable for the whole stay: a question, something unexpected, a last-minute idea — they're who you ask.",
"Elle peut aussi s’occuper du reste": "They can also take care of the rest",
"Ménage en cours de séjour et change du linge": "Mid-stay cleaning and fresh linen",
"Courses déposées avant votre arrivée": "Groceries delivered before you arrive",
"Loisirs, soins et bien-être réservés pour vous": "Activities, treatments and wellbeing booked for you",
"Organisation d’un moment particulier — anniversaire, dîner, demande en mariage":
  "Arranging something special — a birthday, a dinner, a proposal",
"Coups de main du quotidien pendant le séjour": "A hand with day-to-day things during the stay",
"Ces prestations sont facultatives, à convenir directement avec la conciergerie, et facturées séparément.":
  "These are optional, arranged directly with the concierge service, and billed separately.",

# ——— Comment venir ————————————————————————————————————————————
"Comment venir": "Getting here",
"En train": "By train",
"— la gare de Saint-Hilaire-de-Riez est sur la ligne TER Nantes–Saint-Gilles-Croix-de-Vie, à quinze minutes à pied de la maison. Celle de Saint-Gilles est le terminus, à vingt minutes.":
  "— Saint-Hilaire-de-Riez station is on the Nantes–Saint-Gilles-Croix-de-Vie regional line, fifteen minutes' walk from the house. Saint-Gilles is the end of the line, twenty minutes away.",
"En voiture": "By car",
"— environ 1 h 15 de Nantes, 1 h de La Roche-sur-Yon, 4 h 30 de Paris par l’A11 puis l’A83.":
  "— about 1 hr 15 from Nantes, 1 hr from La Roche-sur-Yon, 4 hr 30 from Paris via the A11 then the A83.",
"En avion": "By air",
"— Nantes Atlantique à une heure de route, puis train ou voiture de location.":
  "— Nantes Atlantique is an hour's drive away, then train or hire car.",

# ——— 09 Questions fréquentes —————————————————————————————————
"09 — Questions fréquentes": "09 — Common questions",
"Ce qu’on nous": "What people",
"demande": "ask us",
"souvent": "most",
"Peut-on se passer de voiture ?": "Can we manage without a car?",
"Oui, et c’est même recommandé. Les commerces sont à sept minutes à pied, la corniche à dix, la plage à quinze, le port à vingt. Le train s’arrête à Saint-Hilaire-de-Riez, et l’embarcadère pour l’île d’Yeu est à dix minutes de marche. Une voiture ne sert que pour aller plus loin dans les terres.":
  "Yes, and we'd recommend it. The shops are seven minutes' walk away, the clifftop path ten, the beach fifteen, the harbour twenty. The train stops at Saint-Hilaire-de-Riez, and the Île d'Yeu pier is a ten-minute walk. A car is only useful for going further inland.",
"Que faire quand il pleut ?": "What is there to do when it rains?",
"La Bourrine du Bois Juquaud, Escale Pêche au cœur de la criée, les musées de Saint-Gilles, le marché couvert. Et la maison : les tempêtes vues de la corniche sont un spectacle, et l’on rentre se sécher au chaud.":
  "La Bourrine du Bois Juquaud, Escale Pêche at the fish auction, the museums in Saint-Gilles, the covered market. And the house itself: a storm watched from the clifftop path is worth the trip, and you come back in to dry off in the warm.",
"Combien de personnes peut-on être ?": "How many of us can stay?",
"Deux, et deux seulement. Il y a une chambre avec un lit de 160 cm ; la seconde pièce est un bureau, pas un couchage. C’est un logement pensé pour un couple, ou pour une personne seule qui vient travailler au calme. Les animaux ne sont pas admis.":
  "Two, and only two. There is one bedroom with a 160 cm bed; the second room is a study, not a sleeping room. The house is meant for a couple, or for one person coming to work in peace. Pets are not allowed.",
"Peut-on y travailler quelques semaines ?": "Could we work from here for a few weeks?",
"C’est même une bonne idée hors saison. Le bureau est une pièce fermée avec sa fenêtre, le wifi est en fibre, et un séjour au mois bénéficie de 25 à 30 % de réduction l’hiver. La corniche est à dix minutes pour la pause de midi.":
  "Out of season it's a good idea. The study is a room that shuts, with its own window, the wifi is fibre, and a stay by the month gets 25–30% off in winter. The clifftop path is ten minutes away for a lunch break.",
"Qui nous accueille à l’arrivée ?": "Who meets us when we arrive?",
"Halo Conciergerie, une conciergerie professionnelle de Saint-Gilles-Croix-de-Vie. Elle vous remet les clés, vous fait le tour de la maison et reste joignable pendant tout le séjour. Elle propose aussi, si vous le souhaitez, du ménage en cours de séjour, des courses déposées avant votre arrivée ou l’organisation d’un moment particulier.":
  "Halo Conciergerie, a professional concierge service in Saint-Gilles-Croix-de-Vie. They hand over the keys, show you round the house and stay reachable for the whole stay. If you'd like, they also offer mid-stay cleaning, groceries delivered before you arrive, or help arranging something special.",
"Les draps et serviettes sont-ils fournis ?": "Are bed linen and towels provided?",
"Oui. Le lit est fait à votre arrivée et le linge de toilette vous attend dans la salle d’eau. Vous n’avez rien à apporter.":
  "Yes. The bed is made when you arrive and the towels are waiting in the shower room. There is nothing to bring.",
"Comment réserver, et peut-on annuler ?": "How do we book, and can we cancel?",
"Les réservations passent uniquement par Airbnb : le calendrier y est tenu à jour et les conditions d’annulation sont celles affichées sur l’annonce. Pour une question avant de réserver, la messagerie Airbnb est le plus direct.":
  "Bookings go through Airbnb only: the calendar there is kept up to date and the cancellation terms are the ones shown on the listing. For a question before booking, Airbnb messages are the most direct route.",

# ——— 10 Réserver ——————————————————————————————————————————————
"10 — Réserver": "10 — Book",
"Les dates vivent": "The calendar lives",
"sur": "on",
"Airbnb": "Airbnb",
"Le calendrier et les tarifs y sont tenus à jour au fil des saisons — basse lumière d’hiver, matins de juin, plein été. Quelques clics, et la maison vous attend, volets ouverts.":
  "Dates and prices are kept up to date there through the seasons — low winter light, June mornings, high summer. A few clicks, and the house is waiting for you with the shutters open.",
"à partir de 75 €": "from €75",
"la nuit, selon la saison": "a night, depending on the season",
"Voir les disponibilités sur Airbnb": "See available dates on Airbnb",
"Une question avant de réserver ? La messagerie Airbnb reste le plus simple : on répond vite, et volontiers. Sur place, c’est Halo Conciergerie, à Saint-Gilles-Croix-de-Vie, qui vous accueille et veille au bon déroulement du séjour.":
  "A question before you book? Airbnb messages are the simplest way: we answer quickly, and gladly. On the ground it's Halo Conciergerie, in Saint-Gilles-Croix-de-Vie, who welcome you and keep an eye on the stay.",

# ——— Pied de page et barre mobile —————————————————————————————
"85270 Saint-Hilaire-de-Riez, Vendée": "85270 Saint-Hilaire-de-Riez, Vendée, France",
"Réserver sur Airbnb": "Book on Airbnb",
"Meublé de tourisme n°": "Registered holiday let no.",
"Mentions légales · Conditions de réservation · Confidentialité": "Legal notice · Booking terms · Privacy",
"Vues aériennes © Google": "Aerial views © Google",
"à partir de 75 € la nuit": "from €75 a night",
"2 voyageurs · terrasse et jardin": "2 guests · terrace and garden",

# ——— Visionneuse —————————————————————————————————————————————
"Fermer": "Close",
"Photo agrandie": "Enlarged photo",
"Photo précédente": "Previous photo",
"Photo suivante": "Next photo",

# ——— Descriptions des photos (attribut alt) ——————————————————
"La chambre de La petite vague, mur bleu et lit fait":
  "The bedroom at La petite vague, blue wall and made bed",
"Le séjour ouvert sur la terrasse par une grande baie vitrée":
  "The living room opening onto the terrace through a wide glass door",
"La cuisine équipée et sa grande table de bois clair":
  "The fitted kitchen and its big pale wood table",
"La terrasse en façade, abritée, ouverte sur le séjour":
  "The sheltered terrace at the front, opening onto the living room",
"La maison vue depuis la rue, façade blanche et toit de tuiles":
  "The house from the street, white front and tiled roof",
"Vue aérienne : la maison entre la plage de Boisvinet et le port de Saint-Gilles-Croix-de-Vie":
  "Aerial view: the house between Boisvinet beach and Saint-Gilles-Croix-de-Vie harbour",
"La côte vendéenne, de Saint-Jean-de-Monts aux Sables, avec l’île d’Yeu au large":
  "The Vendée coast, from Saint-Jean-de-Monts to Les Sables, with the Île d'Yeu offshore",
"La chambre, mur bleu, lit fait et coussin de lin":
  "The bedroom, blue wall, made bed and linen cushion",
"Six coquillages peints en blanc, bleu et jaune, suspendus au mur":
  "Six shells painted white, blue and yellow, hung on the wall",
"Deux verres sur la table basse, baie vitrée et jardin au couchant":
  "Two glasses on the coffee table, glass door and garden at sunset",
"La terrasse en façade, baie vitrée ouverte sur le séjour et voile d’ombrage":
  "The front terrace, glass door open onto the living room, and a shade sail",
"Le miroir rond reflétant le lit et la gravure de vague":
  "The round mirror reflecting the bed and the wave print",
"Reflet du dressing et des coquillages dans le miroir rond":
  "The dressing area and the shells reflected in the round mirror",
"La vasque de la salle d’eau sous le miroir rond rétroéclairé":
  "The shower room basin under the backlit round mirror",
"Le séjour au coucher du soleil, fauteuil et table basse devant la baie":
  "The living room at sunset, armchair and coffee table in front of the glass",
"La douche à l’italienne et le miroir rétroéclairé":
  "The walk-in shower and the backlit mirror",
"Le jardin à l’arrière, claustra de bois et haie, en plein soleil":
  "The garden at the back, wooden screen and hedge, in full sun",
"La cuisine ouverte et la grande table de bois clair":
  "The open kitchen and the big pale wood table",
}

# Métadonnées, hors corps de page : titre de l'onglet, description pour les
# moteurs et les aperçus de lien, et la langue déclarée.
META = {
  "titre": "La petite vague — a house for two in Saint-Hilaire-de-Riez",
  "description": "A single-level house for two in Saint-Hilaire-de-Riez, Vendée: private terrace and garden, a study with a door. Clifftop path 10 min on foot. From €75 a night.",
  "og_titre": "La petite vague — a house for two, between sea and marsh",
  "og_description": "Fifty-five square metres for two in Saint-Hilaire-de-Riez: private terrace and garden, a study with a door that shuts, the clifftop path ten minutes away on foot.",
}

# Textes construits par le script de la page (et non présents dans le HTML).
UI = {
  "agrandir": "Enlarge: ",   # préfixe du libellé des photos
  "sur": " of ",             # « 5 sur 18 » → « 5 of 18 »
}
