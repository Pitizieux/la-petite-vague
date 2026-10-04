# -*- coding: utf-8 -*-
"""Esquisse au crayon du rez-de-chaussée — murs seuls.
Géométrie relevée sur le plan Kozikaza du 12/01/2025 (image), murs mesurés au pixel
puis recalés sur les cotes imprimées."""
import math, random

rnd = random.Random(20260104)

M_L, M_T, M_R, M_B = 118, 92, 124, 176
W, H = 805, 900
VB_W, VB_H = W + M_L + M_R, H + M_T + M_B
E, P = 27, 10

MINE   = '#333B37'      # graphite
HACHE  = '#6B736E'      # hachures
COTE   = '#9C5231'
GRIS   = '#5A6A68'
LIN    = '#F4EFE7'

def X(v): return round(v + M_L, 1)
def Y(v): return round(v + M_T, 1)

out = []
def add(t): out.append(t)

# ——————————————————————— trait au crayon ———————————————————————
PAS_PT = 34
def main_levee(x1, y1, x2, y2, amp=1.7, over=3.2):
    """Un seul passage de crayon : léger tremblement et dépassement aux extrémités."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    if L < 1e-6: return ''
    ux, uy = dx / L, dy / L
    px, py = -uy, ux                                     # perpendiculaire
    o1, o2 = rnd.uniform(0, over), rnd.uniform(0, over)
    x1, y1 = x1 - ux * o1, y1 - uy * o1
    x2, y2 = x2 + ux * o2, y2 + uy * o2
    L += o1 + o2
    n = max(3, int(L / PAS_PT) + 2)
    pts, d = [], 0.0
    for i in range(n + 1):
        t = i / n
        e = 0.0 if i in (0, n) else rnd.gauss(0, amp)    # bords tenus
        d = d * 0.55 + e * 0.45                           # bruit lissé
        pts.append((x1 + dx0 * t + px * d, y1 + dy0 * t + py * d) if False else
                   (x1 + (x2 - x1) * t + px * d, y1 + (y2 - y1) * t + py * d))
    s = f'M {X(pts[0][0])},{Y(pts[0][1])}'
    for i in range(1, len(pts) - 1):
        mx, my = (pts[i][0] + pts[i+1][0]) / 2, (pts[i][1] + pts[i+1][1]) / 2
        s += f' Q {X(pts[i][0])},{Y(pts[i][1])} {X(mx)},{Y(my)}'
    s += f' L {X(pts[-1][0])},{Y(pts[-1][1])}'
    return s

def trait(x1, y1, x2, y2, passes=2, w=3.4, amp=2.2, op=0.92, over=7.0, couleur=MINE):
    for k in range(passes):
        d = main_levee(x1, y1, x2, y2, amp=amp * (1 + .35 * k), over=over)
        add(f'<path d="{d}" stroke="{couleur}" stroke-width="{round(w*(1-.22*k),2)}" '
            f'fill="none" stroke-linecap="round" opacity="{round(op*(1-.3*k),2)}"/>')

# ——————————————————————— géométrie ———————————————————————
ext = [(0,0),(W,0),(W,787),(330,787),(330,H),(0,H)]
inn = [(E,E),(W-E,E),(W-E,760),(303,760),(303,H-E),(E,H-E)]

cloisons = [   # x0,y0,x1,y1
 (212, 27, 222, 240), (212, 147, 322, 157), (312, 27, 322, 355),
 ( 27, 240, 222, 250), (212, 250, 222, 428), ( 27, 428, 222, 438),
 (312, 345, 778, 355),
]
# baies : (x0,y0,x1,y1, 'fenetre'|'porte', orientation)
baies = [
 (106,   0, 187,  E, 'fenetre', 'h'), (239,  0, 290,  E, 'fenetre', 'h'),
 (516,   0, 658,  E, 'fenetre', 'h'), (  0, 350,  E, 401, 'fenetre', 'v'),
 (  0, 444,  E, 535, 'porte',   'v'), (467, 760, 675, 787, 'fenetre', 'h'),
 ( 94, 873, 251, H,  'fenetre', 'h'),
 (212,  45, 222, 117, 'porte', 'v'), (232, 147, 300, 157, 'porte', 'h'),
 (312, 245, 322, 333, 'porte', 'v'), ( 52, 428, 122, 438, 'porte', 'h'),
]

def rect_path(x0,y0,x1,y1):
    return f'M {X(x0)},{Y(y0)} L {X(x1)},{Y(y0)} L {X(x1)},{Y(y1)} L {X(x0)},{Y(y1)} Z'
def poly_path(pts):
    return 'M ' + ' L '.join(f'{X(a)},{Y(b)}' for a,b in pts) + ' Z'

# masque = emprise des murs, percements exclus (règle pair-impair)
masque = poly_path(ext) + ' ' + poly_path(inn)
for c in cloisons: masque += ' ' + rect_path(*c)
for b in baies:    masque += ' ' + rect_path(b[0], b[1], b[2], b[3])

add('<defs>')
add(f'<clipPath id="murs" clip-rule="evenodd"><path d="{masque}"/></clipPath>')
add('<filter id="grain" x="-3%" y="-3%" width="106%" height="106%">'
    '<feTurbulence type="fractalNoise" baseFrequency="0.82" numOctaves="2" seed="5" result="n"/>'
    '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.1" '
    'xChannelSelector="R" yChannelSelector="G"/></filter>')
add('</defs>')

add('<g filter="url(#grain)">')

# ——— hachures à 45°, au crayon, dans l’épaisseur des murs ———
bandes = [ (0,0,W,E), (0,0,E,H), (W-E,0,W,787), (303,760,W,787),
           (303,760,330,H), (0,H-E,330,H) ] + [tuple(c) for c in cloisons]

add(f'<path d="{masque}" fill-rule="evenodd" fill="{MINE}" opacity="0.14"/>')
# les cloisons, plus minces, ont besoin d’un peu plus de corps
_cl = ' '.join(rect_path(*c) for c in cloisons)
def _dans_cloison(b):
    return any(b[0] >= c[0]-1 and b[2] <= c[2]+1 and b[1] >= c[1]-1 and b[3] <= c[3]+1
               for c in cloisons)
_pc = ' '.join(rect_path(b[0],b[1],b[2],b[3]) for b in baies if _dans_cloison(b))
add(f'<path d="{_cl} {_pc}" fill-rule="evenodd" fill="{MINE}" opacity="0.10"/>')
add('<g clip-path="url(#murs)">')
PAS_H = 5.4
for bx0, by0, bx1, by1 in bandes:
    c = bx0 + by0
    cmax = bx1 + by1
    while c < cmax:
        xa = max(bx0, c - by1); xb = min(bx1, c - by0)
        if xb - xa > 2:
            d = main_levee(xa, c - xa, xb, c - xb, amp=0.9, over=1.4)
            add(f'<path d="{d}" stroke="{HACHE}" stroke-width="2.2" fill="none" '
                f'stroke-linecap="round" opacity="{round(rnd.uniform(.42,.62),2)}"/>')
        c += PAS_H + rnd.uniform(-.4, .4)
add('</g>')

# ——— arêtes des murs, interrompues aux baies ———
def segments(a, b, coupes):
    """découpe [a,b] en retirant les intervalles de coupes"""
    bouts = [(a, b)]
    for c0, c1 in coupes:
        suite = []
        for s0, s1 in bouts:
            if c1 <= s0 or c0 >= s1: suite.append((s0, s1)); continue
            if c0 > s0: suite.append((s0, c0))
            if c1 < s1: suite.append((c1, s1))
        bouts = suite
    return [(s0, s1) for s0, s1 in bouts if s1 - s0 > 1.5]

def face_h(y, a, b, coupes):
    for s0, s1 in segments(a, b, coupes): trait(s0, y, s1, y)
def face_v(x, a, b, coupes):
    for s0, s1 in segments(a, b, coupes): trait(x, s0, x, s1)

cx = lambda o: [(b[0], b[2]) for b in baies if b[5] == 'h' and abs(b[1]-o) < 40]
cy = lambda o: [(b[1], b[3]) for b in baies if b[5] == 'v' and abs(b[0]-o) < 40]

face_h(0,   0, W,   [(106,187),(239,290),(516,658)])          # nord, extérieur
face_h(E,   E, W-E, [(106,187),(239,290),(516,658)])          # nord, intérieur
face_v(0,   0, H,   [(350,401),(444,535)])                    # ouest, extérieur
face_v(E,   E, H-E, [(350,401),(444,535)])                    # ouest, intérieur
face_v(W,   0, 787, [])                                       # est, extérieur
face_v(W-E, E, 760, [])                                       # est, intérieur
face_h(787, 330, W,   [(467,675)])                            # sud du volume, extérieur
face_h(760, 303, W-E, [(467,675)])                            # sud du volume, intérieur
face_v(330, 787, H,   [])                                     # aile, est extérieur
face_v(303, 760, H-E, [])                                     # aile, est intérieur
face_h(H,   0, 330, [(94,251)])                               # aile, sud extérieur
face_h(H-E, E, 303, [(94,251)])                               # aile, sud intérieur

# tableaux (jambages) de chaque baie
for x0,y0,x1,y1,genre,sens in baies:
    if sens == 'h':
        trait(x0, y0, x0, y1, passes=1, w=1.8, over=1.2)
        trait(x1, y0, x1, y1, passes=1, w=1.8, over=1.2)
        if genre == 'fenetre':
            trait(x0, (y0+y1)/2, x1, (y0+y1)/2, passes=1, w=1.5, amp=1.1, op=.6, over=0)
    else:
        trait(x0, y0, x1, y0, passes=1, w=1.8, over=1.2)
        trait(x0, y1, x1, y1, passes=1, w=1.8, over=1.2)
        if genre == 'fenetre':
            trait((x0+x1)/2, y0, (x0+x1)/2, y1, passes=1, w=1.5, amp=1.1, op=.6, over=0)

# arêtes des cloisons, baies déduites
for x0,y0,x1,y1 in cloisons:
    if (x1-x0) < (y1-y0):                                     # cloison verticale
        c = [(b[1],b[3]) for b in baies if b[5]=='v' and abs(b[0]-x0)<6]
        face_v(x0, y0, y1, c); face_v(x1, y0, y1, c)
    else:
        c = [(b[0],b[2]) for b in baies if b[5]=='h' and abs(b[1]-y0)<6]
        face_h(y0, x0, x1, c); face_h(y1, x0, x1, c)

# ——— cotes, au crayon elles aussi ———
def cote(a0,b0,a1,b1,txt,dec=0,vert=False):
    if vert:
        xx = a0 + dec
        trait(xx, b0, xx, b1, passes=1, w=1.4, amp=1.0, op=.75, over=0, couleur=COTE)
        for bb in (b0,b1):
            trait(xx-9, bb, xx+9, bb, passes=1, w=1.4, amp=.7, op=.75, over=1, couleur=COTE)
        add(f'<text x="{X(xx-14)}" y="{Y((b0+b1)/2)}" fill="{COTE}" font-size="29" '
            f'text-anchor="middle" transform="rotate(-90 {X(xx-14)} {Y((b0+b1)/2)})">{txt}</text>')
    else:
        yy = b0 + dec
        trait(a0, yy, a1, yy, passes=1, w=1.4, amp=1.0, op=.75, over=0, couleur=COTE)
        for aa in (a0,a1):
            trait(aa, yy-9, aa, yy+9, passes=1, w=1.4, amp=.7, op=.75, over=1, couleur=COTE)
        add(f'<text x="{X((a0+a1)/2)}" y="{Y(yy-14)}" fill="{COTE}" font-size="29" '
            f'text-anchor="middle">{txt}</text>')

cote(0, 0, W, 0, '805', dec=-56)
cote(0, 0, 0, H, '900', dec=-62, vert=True)
cote(W, 0, W, 787, '788', dec=62, vert=True)
cote(322, 0, 778, 0, '450', dec=62)
cote(778, 27, 778, 345, '313', dec=-66, vert=True)

add('</g>')   # fin du grain

# ——————————————————————— annotations ———————————————————————
MAIN = 'Architects Daughter, Fraunces, Georgia, serif'
def piece(a, b, nom, aire=None, t=36):
    add(f'<text x="{X(a)}" y="{Y(b)}" fill="{MINE}" font-size="{t}" text-anchor="middle" '
        f'font-family="{MAIN}">{nom}</text>')
    if aire:
        add(f'<text x="{X(a)}" y="{Y(b+33)}" fill="{GRIS}" font-size="25" text-anchor="middle" '
            f'font-family="{MAIN}">{aire}</text>')

piece(121, 150, 'Bureau', '3,7 m²')
piece(267, 100, 'WC', None, 26)
piece(121, 352, 'Salle d’eau', '3,1 m²')
piece(550,  96, 'Chambre', '14,1 m²')
piece(520, 520, 'Séjour et cuisine', '31,8 m²')
add(f'<text x="{X(571)}" y="{Y(735)}" fill="{GRIS}" font-size="23" text-anchor="middle" '
    f'font-family="{MAIN}">baie sur la terrasse</text>')
add(f'<text x="{X(76)}" y="{Y(478)}" fill="{GRIS}" font-size="23" font-family="{MAIN}" '
    f'transform="rotate(-90 {X(76)} {Y(478)})">entrée</text>')

# nord
nx, ny = W + 60, 100
add(f'<g filter="url(#grain)">')
trait(nx, ny-34, nx, ny+26, passes=2, w=2.4, over=2, couleur=GRIS)
trait(nx-13, ny-18, nx, ny-36, passes=2, w=2.4, over=1.5, couleur=GRIS)
trait(nx+13, ny-18, nx, ny-36, passes=2, w=2.4, over=1.5, couleur=GRIS)
add('</g>')
add(f'<text x="{X(nx)}" y="{Y(ny+48)}" fill="{GRIS}" font-size="25" text-anchor="middle" '
    f'font-family="{MAIN}">N</text>')

# échelle
ex, ey = 0, H + 64
add('<g filter="url(#grain)">')
trait(ex, ey, ex+200, ey, passes=1, w=1.8, over=0, couleur=GRIS)
for t in (0, 100, 200):
    trait(ex+t, ey-7, ex+t, ey+7, passes=1, w=1.8, over=1, couleur=GRIS)
add('</g>')
add(f'<text x="{X(ex)}" y="{Y(ey+30)}" fill="{GRIS}" font-size="24" font-family="{MAIN}">0</text>')
add(f'<text x="{X(ex+200)}" y="{Y(ey+30)}" fill="{GRIS}" font-size="24" text-anchor="middle" '
    f'font-family="{MAIN}">2 m</text>')

add(f'<text x="{X(W)}" y="{Y(H+118)}" fill="{GRIS}" font-size="25" text-anchor="end" '
    f'font-family="{MAIN}">rez-de-chaussée · cotes en centimètres</text>')
add(f'<text x="{X(W)}" y="{Y(H+152)}" fill="{MINE}" font-size="31" text-anchor="end" '
    f'font-family="{MAIN}">La petite vague — 55 m²</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W} {VB_H}" role="img" '
       f'aria-label="Plan au crayon du rez-de-chaussée : chambre, bureau, salle d’eau, WC, '
       f'séjour ouvert sur la cuisine, baie sur la terrasse" '
       f'font-family="{MAIN}">\n' + '\n'.join(out) + '\n</svg>\n')
import re as _re
svg = _re.sub(r'(\d)\.0(?=[,\s"])', r'\1', svg)
open('_plan/plan.svg','w',encoding='utf-8').write(svg)
print('viewBox', VB_W, VB_H, '|', len(svg), 'octets')
