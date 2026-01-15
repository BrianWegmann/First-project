# Nutrition Recommendation Program (Python)

The goal of the project is not to build a production-ready system, but to demonstrate:
- clean program structure
- input validation
- basic data persistence
- logical separation of responsibilities
- readable and maintainable Python code

---

## 🧠 Project Overview

The program allows users to:
- enter personal data (age, height, weight)
- calculate their BMI
- select a diet type and food restrictions
- receive meal recommendations based on these criteria
- save user data and load it again later

Multiple users are stored in a single JSON file.

---

## 🧩 Features

- BMI calculation
- Support for multiple diet types:
  - omnivore
  - omnivore without fish
  - pescatarian
  - vegetarian
  - vegan
- Food restrictions:
  - nuts
  - milk
  - gluten
- Input validation for all numeric and choice-based inputs
- Persistent storage using JSON
- Modular program structure

---

## 🗂️ Project Structure

-project_folder/
  - main.py # Program entry point and user flow
  - inputs.py # Input validation and user input handling
  - bmi.py # BMI calculation logic
  - meals.py # Meal definitions and filtering logic
  - storage.py # Saving and loading user data (JSON)
  - users.json # Stored user data (created automatically)
  - README(ger).md
  - README.md

---

## 🧱 Design Decisions

The aim of this project is:
- To keep code clear
- To avoid duplicate code

- To be able to easily change and test all components
