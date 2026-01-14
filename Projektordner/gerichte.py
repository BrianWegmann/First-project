gerichte = [
    {
        "name": "Linsencurry",
        "fleisch": False,
        "fisch": False,
        "milch": False,
        "nuesse": False,
        "gluten": False
    },
    {
        "name": "Lachs mit Reis",
        "fleisch": False,
        "fisch": True,
        "milch": False,
        "nuesse": False,
        "gluten": False
    },
    {
        "name": "Hähnchen mit Nudeln",
        "fleisch": True,
        "fisch": False,
        "milch": False,
        "nuesse": False,
        "gluten": True
    }
]

def ernaehrung_erlaubt(gericht, ernaehrung):
    if ernaehrung == "vegan":
        return not gericht["fleisch"] and not gericht["fisch"] and not gericht["milch"]
    if ernaehrung == "vegetarisch":
        return not gericht["fleisch"] and not gericht["fisch"]
    if ernaehrung == "pescetarisch":
        return not gericht["fleisch"]
    if ernaehrung == "omnivor":
        return True
    if ernaehrung == "omnivor_ohne_fisch":
        return not gericht["fisch"]

    return False

def empfehlungen_finden(ernaehrung, nuesse, milch, gluten):
    passend = []

    for gericht in gerichte:
        if not ernaehrung_erlaubt(gericht, ernaehrung):
            continue
        if not nuesse and gericht["nuesse"]:
            continue
        if not milch and gericht["milch"]:
            continue
        if not gluten and gericht["gluten"]:
            continue

        passend.append(gericht["name"])

    return passend
