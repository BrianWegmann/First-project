def berechne_bmi(gewicht, groesse_cm):
    groesse_m = groesse_cm / 100
    bmi = gewicht / (groesse_m ** 2)
    return round(bmi, 1)


def bmi_kategorie(bmi):
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"
