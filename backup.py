import shutil
import os

DATA_FOLDER = "data"

def backup_table():
    table_name = input("Table name to backup: ").strip()
    path = os.path.join(DATA_FOLDER, f"{table_name}.json")
    backup_path = os.path.join(DATA_FOLDER, f"{table_name}.bak.json")
    if not os.path.exists(path):
        print("❌ Table not found.")
        return
    shutil.copy(path, backup_path)
    print("✅ Backup created.")

def restore_table():
    confirmation = input("Restores your table from last backup, so you'll lose all the changes you made after the last backup. Do you want to continue? (y/n): ").strip().lower()
    if confirmation != "y":
        print("❌ Backup not restored.")
        return
    table_name = input("Table name to restore: ").strip()
    backup_path = os.path.join(DATA_FOLDER, f"{table_name}.bak.json")
    path = os.path.join(DATA_FOLDER, f"{table_name}.json")
    if not os.path.exists(backup_path):
        print("❌ Backup not found.")
        return
    shutil.copy(backup_path, path)
    print("✅ Table restored from backup.")
