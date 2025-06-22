import json
import os
from colorama import Fore, Style

DATA_FOLDER = "data"

def ensure_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_table(table_name, data):
    path = os.path.join(DATA_FOLDER, f"{table_name}.json")
    save_json(path, data)

def load_table():
    ensure_data_folder()
    table_name = input("Enter table name: ").strip().lower()
    file_path = os.path.join(DATA_FOLDER, f"{table_name}.json")
    if not os.path.exists(file_path):
        print(Fore.RED + "❌ Table not found." + Style.RESET_ALL)
        return None
    data = load_json(file_path)
    data["name"] = table_name
    return data

def print_table(fields, records):
    if not records:
        print(Fore.YELLOW + "📭 No records found." + Style.RESET_ALL)
        return

    print("\n" + "-" * 60)
    print(" | ".join(fields))
    print("-" * 60)
    for record in records:
        print(" | ".join(str(record.get(f, "")) for f in fields))
    print("-" * 60 + "\n")
