import json
import os

FILE_NAME = "users.json"


def load_all_users():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_all_users(users):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def save_user(name, data):
    users = load_all_users()
    users[name] = data
    save_all_users(users)


def load_user(name):
    users = load_all_users()
    return users.get(name)
