import json

FILE = "users.json"


def load_users():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


def signup(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username:
            return False  # already exists

    users.append({
        "username": username,
        "password": password
    })

    save_users(users)
    return True


def login(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

    return False