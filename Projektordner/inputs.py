def input_float(text, min_value, max_value):
    while True:
        user_input = input(f"{text}: ").replace(",", ".").strip()

        try:
            value = float(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < min_value or value > max_value:
            print(f"Value must be between {min_value} and {max_value}.")
            continue

        return value


def input_int(text, min_value, max_value):
    while True:
        user_input = input(f"{text}: ").strip()

        if not user_input.isdigit():
            print("Please enter a whole number.")
            continue

        value = int(user_input)

        if value < min_value or value > max_value:
            print(f"Value must be between {min_value} and {max_value}.")
            continue

        return value


def input_choice(text, options):
    options_lower = [o.lower() for o in options]

    while True:
        user_input = input(f"{text} ({'/'.join(options)}): ").strip().lower()

        if user_input in options_lower:
            return user_input

        print("Invalid input.")


def input_yes_no(text):
    while True:
        user_input = input(f"{text} (yes/no): ").strip().lower()

        if user_input in ["yes", "y"]:
            return True
        if user_input in ["no", "n"]:
            return False

        print("Please enter 'yes' or 'no'.")
