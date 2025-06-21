import json, os

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
        print("❌ Table not found.")
        return None

    data = load_json(file_path)
    data["name"] = table_name
    return data

def print_table(fields, records):
    if not records:
        print("📭 No records found.")
        return

    print("\n" + "-" * 40)
    print(" | ".join(fields))
    print("-" * 40)
    for record in records:
        print(" | ".join(record.get(f, "") for f in fields))
    print("-" * 40 + "\n")
