def eingabe_float(text, min_wert, max_wert):
    while True:
        eingabe = input(f"{text}: ").replace(",", ".").strip()

        try:
            wert = float(eingabe)
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
            continue

        if wert < min_wert or wert > max_wert:
            print(f"Wert muss zwischen {min_wert} und {max_wert} liegen.")
            continue

        return wert


def eingabe_int(text, min_wert, max_wert):
    while True:
        eingabe = input(f"{text}: ").strip()

        if not eingabe.isdigit():
            print("Bitte eine ganze Zahl eingeben.")
            continue

        wert = int(eingabe)

        if wert < min_wert or wert > max_wert:
            print(f"Wert muss zwischen {min_wert} und {max_wert} liegen.")
            continue

        return wert


def eingabe_auswahl(text, optionen):
    optionen_lower = [o.lower() for o in optionen]

    while True:
        eingabe = input(f"{text} ({'/'.join(optionen)}): ").strip().lower()

        if eingabe in optionen_lower:
            return eingabe

        print("Ungültige Eingabe")


def eingabe_ja_nein(text):
    while True:
        eingabe = input(f"{text} (ja/nein): ").strip().lower()

        if eingabe in ["ja", "j"]:
            return True
        if eingabe in ["nein", "n"]:
            return False

        print("Bitte 'ja' oder 'nein' eingeben")
