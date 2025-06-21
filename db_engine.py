import json, os
from utils import *

DATA_FOLDER = "data"

def create_table():
    table_name = input("Enter table name: ").strip().lower()
    file_path = os.path.join(DATA_FOLDER, f"{table_name}.json")

    if os.path.exists(file_path):
        print("⚠️ Table already exists.")
        return

    fields = input("Enter column names (comma-separated): ").split(",")
    fields = [f.strip() for f in fields]
    save_json(file_path, {"fields": fields, "records": []})
    print(f"✅ Table '{table_name}' created.")

def insert_record():
    table = load_table()
    if not table: return

    record = {}
    for field in table["fields"]:
        record[field] = input(f"{field}: ")

    table["records"].append(record)
    save_table(table["name"], table)
    print("✅ Record inserted.")

def view_records():
    table = load_table()
    if not table: return

    print_table(table["fields"], table["records"])

def update_record():
    table = load_table()
    if not table: return

    key = input("Search by which field? ")
    value = input("Value to match: ")

    updated = False
    for record in table["records"]:
        if record.get(key) == value:
            print("🎯 Match found: ", record)
            for field in table["fields"]:
                new_val = input(f"New {field} (leave blank to keep '{record[field]}'): ")
                if new_val:
                    record[field] = new_val
            updated = True
            break

    if updated:
        save_table(table["name"], table)
        print("✅ Record updated.")
    else:
        print("❌ No matching record.")

def delete_record():
    table = load_table()
    if not table: return

    key = input("Delete by which field? ")
    value = input("Value to match: ")

    before = len(table["records"])
    table["records"] = [r for r in table["records"] if r.get(key) != value]

    if len(table["records"]) < before:
        save_table(table["name"], table)
        print("🗑️ Record deleted.")
    else:
        print("❌ No match found.")

def search_records():
    table = load_table()
    if not table: return

    key = input("Search by which field? ")
    value = input("Value to match: ")

    matches = [r for r in table["records"] if r.get(key) == value]
    print_table(table["fields"], matches)
