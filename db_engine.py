import os
import datetime
import csv
from utils import *

def create_table():
    table_name = input("Enter table name: ").strip().lower()
    file_path = os.path.join("data", f"{table_name}.json")

    if os.path.exists(file_path):
        print("⚠️ Table already exists.")
        return

    fields = []
    types = {}
    num_fields = int(input("How many fields? "))
    for _ in range(num_fields):
        name = input("Field name: ").strip()
        dtype = input("Type (str/int/float/bool): ").strip().lower()
        fields.append(name)
        types[name] = dtype

    save_json(file_path, {"fields": fields, "types": types, "records": []})
    print(f"✅ Table '{table_name}' created.")

def validate_input(value, dtype):
    try:
        if dtype == "int":
            return int(value)
        elif dtype == "float":
            return float(value)
        elif dtype == "bool":
            return value.lower() in ["true", "1"]
        return value
    except:
        print("❌ Invalid data type.")
        return None

def insert_record():
    table = load_table()
    if not table:
        return

    record = {}
    for field in table["fields"]:
        raw = input(f"{field} ({table['types'][field]}): ")
        value = validate_input(raw, table["types"][field])
        if value is None:
            return
        record[field] = value

    record["created_at"] = datetime.datetime.now().isoformat()
    table["records"].append(record)
    save_table(table["name"], table)
    print("✅ Record inserted.")

def view_records():
    table = load_table()
    if not table:
        return
    print_table(table["fields"], table["records"])

def update_record():
    table = load_table()
    if not table:
        return

    key = input("Search by which field? ")
    value = input("Value to match: ")

    updated = False
    for record in table["records"]:
        if str(record.get(key)) == value:
            print("🎯 Match found: ", record)
            for field in table["fields"]:
                new_val = input(f"New {field} (blank = keep '{record[field]}'): ")
                if new_val:
                    validated = validate_input(new_val, table["types"][field])
                    if validated is not None:
                        record[field] = validated
            record["updated_at"] = datetime.datetime.now().isoformat()
            updated = True
            break

    if updated:
        save_table(table["name"], table)
        print("✅ Record updated.")
    else:
        print("❌ No match found.")

def delete_record():
    table = load_table()
    if not table:
        return

    key = input("Delete by which field? ")
    value = input("Value to match: ")

    before = len(table["records"])
    table["records"] = [r for r in table["records"] if str(r.get(key)) != value]

    if len(table["records"]) < before:
        save_table(table["name"], table)
        print("🗑️ Record deleted.")
    else:
        print("❌ No match found.")

def search_records():
    table = load_table()
    if not table:
        return

    key = input("Search by which field? ")
    value = input("Value to match: ")

    matches = [r for r in table["records"] if str(r.get(key)) == value]
    print_table(table["fields"], matches)

def export_to_csv():
    table = load_table()
    if not table:
        return

    filename = f"{table['name']}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=table["fields"])
        writer.writeheader()
        # Filter records to only include original fields
        filtered_records = []
        for record in table["records"]:
            filtered_record = {field: record.get(field, "") for field in table["fields"]}
            filtered_records.append(filtered_record)
        writer.writerows(filtered_records)
    print(f"✅ Exported to {filename}")
