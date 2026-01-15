from inputs import *
from bmi import *
from meals import *
from storage import *


def display_result(data):
    print("\n--- Personal Summary ---")
    print(f"Name: {data['name']}")
    print(f"BMI: {data['bmi']} ({data['bmi_category']})")

    print("\nRecommended meals:")
    if data["recommendations"]:
        for meal in data["recommendations"]:
            print(f"- {meal}")
    else:
        print("No suitable meals found.")


def new_user():
    name = input("Name: ").strip()

    age = input_int("Age", 10, 120)
    height = input_float("Height in cm", 120, 230)
    weight = input_float("Weight in kg", 30, 300)

    diet = input_choice(
        "Diet type",
        ["omnivore", "omnivore_no_fish", "pescatarian", "vegetarian", "vegan"]
    )

    nuts = input_yes_no("May it contain nuts?")
    milk = input_yes_no("May it contain milk?")
    gluten = input_yes_no("May it contain foods containing gluten?")

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    recommendations = find_recommendations(
        diet, nuts, milk, gluten
    )

    user_data = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "bmi_category": category,
        "diet": diet,
        "nuts": nuts,
        "milk": milk,
        "gluten": gluten,
        "recommendations": recommendations
    }

    save_user(name, user_data)
    display_result(user_data)


def existing_user():
    name = input("Name: ").strip()
    data = load_user(name)

    if data is None:
        print("No user found.")
        return

    display_result(data)


def main():
    print("Welcome to the nutrition program")

    choice = input_choice(
        "New or existing user?",
        ["new", "existing"]
    )

    if choice == "new":
        new_user()
    else:
        existing_user()


if __name__ == "__main__":
    main()
