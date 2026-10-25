"""Met à jour /disponibilites.json à partir du calendrier iCal exporté par Airbnb.

Lancé toutes les trois heures par GitHub Actions (.github/workflows/disponibilites.yml).
L'adresse iCal n'est jamais écrite dans le dépôt : elle vient du secret AIRBNB_ICAL.

Le fichier produit ne contient que des plages de nuits occupées, sans aucun nom :
  {"maj": "2026-10-25T16:00:00Z", "occupe": [["2026-11-02", "2026-11-05"], ...]}
Chaque plage va de la première nuit occupée (incluse) au jour de départ (exclu),
exactement comme DTSTART / DTEND dans le fichier iCal.

Usage : python3 maj.py <url-ou-fichier.ics> <sortie.json>
"""
import datetime as dt
import json
import sys
import urllib.request

HORIZON_JOURS = 550  # environ 18 mois devant nous


def lire(source):
    if source.startswith("http"):
        req = urllib.request.Request(source, headers={"User-Agent": "la-petite-vague/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace")
    with open(source, encoding="utf-8") as f:
        return f.read()


def date_ical(valeur):
    # 20261102 ou 20261102T150000Z : seule la date compte pour des nuits
    return dt.date(int(valeur[0:4]), int(valeur[4:6]), int(valeur[6:8]))


def plages(texte):
    # Dépliage des lignes longues (RFC 5545 : une ligne qui commence par un espace continue la précédente)
    lignes = texte.replace("\r\n ", "").replace("\n ", "").splitlines()
    evts, cour = [], None
    for l in lignes:
        if l == "BEGIN:VEVENT":
            cour = {}
        elif l == "END:VEVENT":
            if cour and "debut" in cour:
                fin = cour.get("fin") or cour["debut"] + dt.timedelta(days=1)
                if fin > cour["debut"]:
                    evts.append((cour["debut"], fin))
            cour = None
        elif cour is not None and ":" in l:
            cle, val = l.split(":", 1)
            nom = cle.split(";")[0]
            if nom == "DTSTART":
                cour["debut"] = date_ical(val.strip())
            elif nom == "DTEND":
                cour["fin"] = date_ical(val.strip())
    return evts


def fusionner(evts):
    aujourdhui = dt.date.today()
    limite = aujourdhui + dt.timedelta(days=HORIZON_JOURS)
    evts = sorted((max(a, aujourdhui - dt.timedelta(days=1)), min(b, limite))
                  for a, b in evts if b > aujourdhui - dt.timedelta(days=1) and a < limite)
    res = []
    for a, b in evts:
        if res and a <= res[-1][1]:
            res[-1][1] = max(res[-1][1], b)
        else:
            res.append([a, b])
    return [[a.isoformat(), b.isoformat()] for a, b in res]


def main():
    source, sortie = sys.argv[1], sys.argv[2]
    texte = lire(source)
    if "BEGIN:VCALENDAR" not in texte:
        sys.exit("Réponse inattendue : ce n'est pas un calendrier iCal.")
    donnees = {
        "maj": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "occupe": fusionner(plages(texte)),
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    print(f"{len(donnees['occupe'])} plage(s) occupée(s) écrite(s) dans {sortie}")


if __name__ == "__main__":
    main()
