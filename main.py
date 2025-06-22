from auth import login_user, register_user
from db_engine import *
from backup import backup_table, restore_table

def auth_flow():
    print("===== USER AUTHENTICATION =====")
    print("1. Login")
    print("2. Register")
    choice = input("Enter choice (1/2): ").strip()
    if choice == "1":
        return login_user()
    elif choice == "2":
        registered = register_user()
        return login_user() if registered else None
    else:
        print("Invalid choice.")
        return None

def print_menu():
    print("""
========= MINI DATABASE ENGINE =========
1. Create Table
2. Insert Record
3. View Records
4. Update Record
5. Delete Record
6. Search Records
7. Export Table to CSV
8. Backup Table
9. Restore Table
10. Exit
""")

def main():
    user = auth_flow()
    if not user:
        return 

    while True:
        print_menu()
        choice = input("Enter choice (1-10): ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_record()
        elif choice == "3":
            view_records()
        elif choice == "4":
            update_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            search_records()
        elif choice == "7":
            export_to_csv()
        elif choice == "8":
            backup_table()
        elif choice == "9":
            restore_table()
        elif choice == "10":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
