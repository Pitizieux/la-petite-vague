# -*- coding: utf-8 -*-
"""Esquisse du rez-de-chaussée — géométrie relevée sur le plan Kozikaza du 12/01/2025."""

M_L, M_T, M_R, M_B = 112, 86, 118, 192          # marges (cm du dessin)
W, H = 805, 900                                  # emprise extérieure
VB_W, VB_H = W + M_L + M_R, H + M_T + M_B
E = 27                                           # mur extérieur
P = 10                                           # cloison

LIN, MARIN, TERRE, ECUME = '#F4EFE7', '#23403C', '#9C5231', '#E8B79A'
GRIS, CRAIE = '#5A6A68', '#C9BFAE'

def x(v): return round(v + M_L, 1)
def y(v): return round(v + M_T, 1)

s = []
def add(t): s.append(t)

# ——— murs extérieurs : poché en evenodd ———
ext = [(0,0),(W,0),(W,787),(330,787),(330,H),(0,H)]
inn = [(E,E),(W-E,E),(W-E,760),(303,760),(303,H-E),(E,H-E)]
def poly(pts): return 'M ' + ' L '.join(f'{x(a)},{y(b)}' for a,b in pts) + ' Z'
add(f'<path d="{poly(ext)} {poly(inn)}" fill="{MARIN}" fill-rule="evenodd"/>')

# ——— cloisons ———
cloisons = [
 (212,  27, P, 213), (212, 147, 110, P), (312,  27, P, 328),
 ( 27, 240, 195, P), (212, 250, P, 188), ( 27, 428, 195, P),
 (312, 345, 466, P),
]
for a,b,w,h in cloisons:
    add(f'<rect x="{x(a)}" y="{y(b)}" width="{w}" height="{h}" fill="{MARIN}"/>')

# ——— percements : on efface le mur puis on retrace l’allège ———
def baie(a,b,w,h, vertical=False, porte=False):
    add(f'<rect x="{x(a)}" y="{y(b)}" width="{w}" height="{h}" fill="{LIN}"/>')
    if porte: return
    if vertical:
        cx = a + w/2
        add(f'<line x1="{x(cx)}" y1="{y(b)}" x2="{x(cx)}" y2="{y(b+h)}" stroke="{MARIN}" stroke-width="3"/>')
    else:
        cy = b + h/2
        add(f'<line x1="{x(a)}" y1="{y(cy)}" x2="{x(a+w)}" y2="{y(cy)}" stroke="{MARIN}" stroke-width="3"/>')

baie(106,   0,  81, E)          # fenêtre bureau
baie(239,   0,  51, E)          # fenêtre wc
baie(516,   0, 142, E)          # fenêtre chambre
baie(  0, 350,  E, 51, True)    # fenêtre salle d’eau
baie(  0, 444,  E, 91, True, porte=True)   # porte d’entrée
baie(467, 760, 208, E)          # baie du séjour
baie( 94, 873, 157, E)          # fenêtre cuisine

# portes intérieures + arcs de débattement
def porte(a,b,w,h, cx,cy, r, a0,a1):
    add(f'<rect x="{x(a)}" y="{y(b)}" width="{w}" height="{h}" fill="{LIN}"/>')
    import math
    x0,y0 = cx+r*math.cos(math.radians(a0)), cy+r*math.sin(math.radians(a0))
    x1,y1 = cx+r*math.cos(math.radians(a1)), cy+r*math.sin(math.radians(a1))
    add(f'<path d="M {x(cx)},{y(cy)} L {x(x0)},{y(y0)} A {r},{r} 0 0 1 {x(x1)},{y(y1)} Z" '
        f'fill="none" stroke="{CRAIE}" stroke-width="2"/>')

porte(212,  45, P, 72, 212, 117, 72, -90, 0)    # bureau
porte(232, 147, 68, P, 232, 147, 68,   0, 90)   # wc
porte( 52, 428, 70, P, 122, 428, 70,  90, 180)  # salle d’eau

# ——— mobilier, trait léger ———
def g(*t): add('<g fill="none" stroke="'+CRAIE+'" stroke-width="2.4" stroke-linejoin="round">'+''.join(t)+'</g>')
def R(a,b,w,h,rx=0): return f'<rect x="{x(a)}" y="{y(b)}" width="{w}" height="{h}" rx="{rx}"/>'
def C(a,b,r): return f'<circle cx="{x(a)}" cy="{y(b)}" r="{r}"/>'
def L(a,b,c,d): return f'<line x1="{x(a)}" y1="{y(b)}" x2="{x(c)}" y2="{y(d)}"/>'

# chambre : lit 160 tête au sud, chevets de part et d’autre
g(R(470,145,160,200,4), L(470,292,630,292), R(424,300,42,45,3), R(634,300,42,45,3))
# bureau : plan de travail sous la fenêtre, siège
g(R(40,40,122,58,3), C(101,124,21))
# salle d’eau : douche, vasque
g(R(32,252,86,86,3), C(75,295,7), R(132,256,68,44,3), C(166,278,11))
# wc
g(R(246,42,38,54,9))
# cuisine en L : plan le long du mur ouest, puis le long du mur sud de l’aile
g(R(32,566,64,297,2), L(32,676,96,676), L(32,760,96,760), C(64,620,21),
  R(96,808,207,55,2), L(176,808,176,863), R(118,818,52,36,3))
# table et tabourets, dans l’aile
g(R(150,636,142,128,3), C(126,666,18), C(126,734,18), C(316,666,18), C(316,734,18))
# séjour : fauteuil, pouf, table basse, meuble bas devant la baie
g(C(612,600,58), R(686,520,72,140,5), R(470,528,58,58,20))
# ——— cotes ———
def cote(a0,b0,a1,b1, txt, dec=0, vert=False):
    if vert:
        xx = a0 + dec
        add(f'<line x1="{x(xx)}" y1="{y(b0)}" x2="{x(xx)}" y2="{y(b1)}" stroke="{TERRE}" stroke-width="1.6"/>')
        for bb in (b0,b1):
            add(f'<line x1="{x(xx-9)}" y1="{y(bb)}" x2="{x(xx+9)}" y2="{y(bb)}" stroke="{TERRE}" stroke-width="1.6"/>')
        add(f'<text x="{x(xx-13)}" y="{y((b0+b1)/2)}" fill="{TERRE}" font-size="26" '
            f'text-anchor="middle" transform="rotate(-90 {x(xx-13)} {y((b0+b1)/2)})">{txt}</text>')
    else:
        yy = b0 + dec
        add(f'<line x1="{x(a0)}" y1="{y(yy)}" x2="{x(a1)}" y2="{y(yy)}" stroke="{TERRE}" stroke-width="1.6"/>')
        for aa in (a0,a1):
            add(f'<line x1="{x(aa)}" y1="{y(yy-9)}" x2="{x(aa)}" y2="{y(yy+9)}" stroke="{TERRE}" stroke-width="1.6"/>')
        add(f'<text x="{x((a0+a1)/2)}" y="{y(yy-13)}" fill="{TERRE}" font-size="26" text-anchor="middle">{txt}</text>')

cote(0, 0, W, 0, '805', dec=-52)
cote(0, 0, 0, H, '900', dec=-58, vert=True)
cote(W, 0, W, 787, '788', dec=58, vert=True)
cote(322, 0, 778, 0, '450', dec=58)
cote(778, 27, 778, 345, '313', dec=-62, vert=True)
cote(27, H, 303, H, '300', dec=44)

# ——— textes des pièces ———
def piece(a,b,nom,aire=None,taille=34):
    add(f'<text x="{x(a)}" y="{y(b)}" fill="{MARIN}" font-size="{taille}" text-anchor="middle" '
        f'font-family="Fraunces, Georgia, serif">{nom}</text>')
    if aire:
        add(f'<text x="{x(a)}" y="{y(b+30)}" fill="{GRIS}" font-size="23" text-anchor="middle" '
            f'letter-spacing="1.6">{aire}</text>')

piece(121, 150, 'Bureau', '3,7 m²')
piece(266,  98, 'WC', None, 24)
piece(121, 360, 'Salle d’eau', '3,1 m²')
piece(550,  92, 'Chambre', '14,1 m²')
piece(500, 428, 'Séjour et cuisine', '31,8 m²')
add(f'<text x="{x(571)}" y="{y(735)}" fill="{GRIS}" font-size="20" text-anchor="middle" '
    f'letter-spacing="2.2">BAIE SUR LA TERRASSE</text>')
add(f'<text x="{x(76)}" y="{y(478)}" fill="{GRIS}" font-size="20" letter-spacing="2.2" '
    f'transform="rotate(-90 {x(76)} {y(478)})">ENTRÉE</text>')

# ——— nord, échelle, cartouche ———
nx, ny = W + 56, 96
add(f'<g stroke="{GRIS}" fill="none" stroke-width="2"><circle cx="{x(nx)}" cy="{y(ny)}" r="30"/>'
    f'<path d="M {x(nx)},{y(ny-18)} L {x(nx-9)},{y(ny+2)} L {x(nx)},{y(ny-4)} L {x(nx+9)},{y(ny+2)} Z" fill="{GRIS}"/></g>')
add(f'<text x="{x(nx)}" y="{y(ny+25)}" fill="{GRIS}" font-size="22" text-anchor="middle">N</text>')

ex, ey = 0, H + 62
add(f'<g stroke="{GRIS}" stroke-width="2"><line x1="{x(ex)}" y1="{y(ey)}" x2="{x(ex+200)}" y2="{y(ey)}"/>'
    f'<line x1="{x(ex)}" y1="{y(ey-7)}" x2="{x(ex)}" y2="{y(ey+7)}"/>'
    f'<line x1="{x(ex+100)}" y1="{y(ey-5)}" x2="{x(ex+100)}" y2="{y(ey+5)}"/>'
    f'<line x1="{x(ex+200)}" y1="{y(ey-7)}" x2="{x(ex+200)}" y2="{y(ey+7)}"/></g>')
add(f'<text x="{x(ex)}" y="{y(ey+28)}" fill="{GRIS}" font-size="21">0</text>')
add(f'<text x="{x(ex+200)}" y="{y(ey+28)}" fill="{GRIS}" font-size="21" text-anchor="middle">2 m</text>')
add(f'<text x="{x(W)}" y="{y(H+128)}" fill="{GRIS}" font-size="22" text-anchor="end" '
    f'letter-spacing="2.4">REZ-DE-CHAUSSÉE · COTES EN CENTIMÈTRES</text>')
add(f'<text x="{x(W)}" y="{y(H+158)}" fill="{MARIN}" font-size="27" text-anchor="end" '
    f'font-family="Fraunces, Georgia, serif" font-style="italic">La petite vague — 55 m²</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W} {VB_H}" '
       f'role="img" aria-label="Plan du rez-de-chaussée : chambre, bureau, salle d’eau, WC, '
       f'séjour ouvert sur la cuisine, baie sur la terrasse" '
       f'font-family="Jost, Helvetica Neue, Arial, sans-serif">\n'
       + '\n'.join(s) + '\n</svg>\n')
open('_plan/plan.svg','w',encoding='utf-8').write(svg)
print('viewBox', VB_W, VB_H, '|', len(svg), 'octets')
