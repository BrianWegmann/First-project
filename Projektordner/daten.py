import json
import os

DATEI = "nutzer.json"


def lade_alle():
    if not os.path.exists(DATEI):
        return {}
    with open(DATEI, "r", encoding="utf-8") as f:
        return json.load(f)


def speichere_nutzer(name, daten):
    alle = lade_alle()
    alle[name] = daten

    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(alle, f, indent=4, ensure_ascii=False)


def lade_nutzer(name):
    alle = lade_alle()
    return alle.get(name)
