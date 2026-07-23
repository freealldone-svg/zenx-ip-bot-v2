import json
import os

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def add_user(user_id):
    users = load_users()

    uid = str(user_id)

    if uid not in users:
        users[uid] = {
            "balance": 0,
            "history": [],
            "banned": False
        }

        save_users(users)
