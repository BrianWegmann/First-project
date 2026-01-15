MEALS = [
    {
        "name": "Vegetable Stir Fry",
        "meat": False,
        "fish": False,
        "nuts": False,
        "milk": False,
        "gluten": True
    },
    {
        "name": "Salmon with Rice",
        "meat": False,
        "fish": True,
        "nuts": False,
        "milk": False,
        "gluten": False
    },
    {
        "name": "Cheese Pasta",
        "meat": False,
        "fish": False,
        "nuts": False,
        "milk": True,
        "gluten": True
    },
    {
        "name": "Quinoa Chickpea Bowl",
        "meat": False,
        "fish": False,
        "nuts": False,
        "milk": False,
        "gluten": False
    },
    {
        "name": "Peanut Tofu Noodles",
        "meat": False,
        "fish": False,
        "nuts": True,
        "milk": False,
        "gluten": True
    },
    {
        "name": "Chicken Curry with Rice",
        "meat": True,
        "fish": False,
        "nuts": False,
        "milk": False,
        "gluten": False
    }
]
def diet_allows(diet, meal):
    if diet == "vegan" and (meal["meat"] or meal["fish"] or meal["milk"]):
        return False
    if diet == "vegetarian" and (meal["meat"] or meal["fish"]):
        return False
    if diet == "pescatarian" and meal["meat"]:
        return False
    if diet == "omnivore_no_fish" and meal["fish"]:
        return False

    return True
def find_recommendations(diet, allow_nuts, allow_milk, allow_gluten):
    recommendations = []

    for meal in MEALS:
        if not diet_allows(diet, meal):
            continue
        if not allow_nuts and meal["nuts"]:
            continue
        if not allow_milk and meal["milk"]:
            continue
        if not allow_gluten and meal["gluten"]:
            continue

        recommendations.append(meal["name"])

    return recommendations