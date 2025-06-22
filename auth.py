import hashlib
import json
import os

USER_FILE = "data/users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user():
    users = load_users()
    username = input("👤 New Username: ").strip()
    if username in users:
        print("⚠️ Username already exists.")
        return False

    password = input("🔒 Password: ")
    users[username] = hash_password(password)
    save_users(users)
    print("✅ User registered successfully!")
    return True

def login_user():
    users = load_users()
    username = input("👤 Username: ").strip()
    password = input("🔑 Password: ")
    if username in users and users[username] == hash_password(password):
        print(f"✅ Welcome back, {username}!\n")
        return username
    print("❌ Login failed. Try again.")
    return None
