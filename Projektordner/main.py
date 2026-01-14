from eingaben import *
from bmi import *
from gerichte import *
from daten import *

def main():
    print("Willkommen beim Ernährungsprogramm")

    auswahl = eingabe_auswahl(
        "Neuer oder bestehender Nutzer?",
        ["neu", "bestehend"]
    )

    if auswahl == "neu":
        neuer_nutzer()
    else:
        bestehender_nutzer()

def ausgabe(daten):
    print("\n--- Persönliche Auswertung ---")
    print(f"Name: {daten['name']}")
    print(f"BMI: {daten['bmi']} ({daten['bmi_kategorie']})")

    print("\nEmpfohlene Gerichte:")
    if daten["empfehlungen"]:
        for gericht in daten["empfehlungen"]:
            print(f"- {gericht}")
    else:
        print("Keine passenden Gerichte gefunden.")


def neuer_nutzer():
    name = input("Name: ").strip()

    alter = eingabe_int("Alter", 10, 120)
    groesse = eingabe_float("Größe in cm", 120, 230)
    gewicht = eingabe_float("Gewicht in kg", 30, 300)

    ernaehrung = eingabe_auswahl(
        "Ernährungsform",
        ["omnivor", "omnivor_ohne_fisch", "pescetarisch", "vegetarisch", "vegan"]
    )

    nuesse = eingabe_ja_nein("Darf Nüsse enthalten?")
    milch = eingabe_ja_nein("Darf Milch enthalten?")
    gluten = eingabe_ja_nein("Darf Gluten enthalten?")

    bmi = berechne_bmi(gewicht, groesse)
    kategorie = bmi_kategorie(bmi)

    empfehlungen = empfehlungen_finden(
        ernaehrung, nuesse, milch, gluten
    )

    daten = {
        "name": name,
        "alter": alter,
        "groesse": groesse,
        "gewicht": gewicht,
        "bmi": bmi,
        "bmi_kategorie": kategorie,
        "ernaehrung": ernaehrung,
        "nuesse": nuesse,
        "milch": milch,
        "gluten": gluten,
        "empfehlungen": empfehlungen
    }

    speichere_nutzer(name, daten)
    ausgabe(daten)


def bestehender_nutzer():
    name = input("Name: ").strip()
    daten = lade_nutzer(name)

    if daten is None:
        print("Kein Nutzer gefunden.")
        return

    ausgabe(daten)

if __name__ == "__main__":
    main()