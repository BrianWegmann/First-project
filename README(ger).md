# Ernährungs- und Empfehlungssystem (Python)

## 🧠 Projektübersicht

Das Programm ermöglicht es Nutzerinnen und Nutzern:

- persönliche Daten einzugeben (Alter, Größe, Gewicht)
- den BMI zu berechnen
- eine Ernährungsform und Unverträglichkeiten anzugeben
- passende Gerichte empfohlen zu bekommen
- ihre Daten zu speichern und später erneut abzurufen

Mehrere Nutzer werden gemeinsam in einer JSON-Datei gespeichert

---

## 🧩 Funktionen

- BMI-Berechnung und Klassifizierung
- Unterstützung verschiedener Ernährungsformen:
  - omnivor
  - omnivor ohne Fisch
  - pescetarisch
  - vegetarisch
  - vegan
- Berücksichtigung von Unverträglichkeiten:
  - Nüsse
  - Milch
  - Gluten
- Eingabevalidierung
- Speicherung der Nutzerdaten
- Trennung der Komponenten

---

## 🗂️ Projektstruktur

Projektordner/
│
├── main.py # Hauptsteuerung
├── inputs.py # Eingabe- und Validierungsfunktionen
├── bmi.py # BMI-Berechnung & Einordnung
├── meals.py # Gerichte und Filterlogik
├── storage.py # Laden und Speichern der Nutzerdaten (JSON)
├── users.json # Nutzerdaten (wird automatisch erstellt)
├── README(ger).md
└── README.md

---

## 🧱 Designentscheidungen

Ziel dieses Projekts ist:
- Code übersichtlich halten
- Doppelten Code zu vermeiden
- Sämtliche Bausteine leicht ändern und testen zu können