from db_engine import *

def print_menu():
    print("""
========= MINI DATABASE ENGINE =========
1. Create Table
2. Insert Record
3. View Records
4. Update Record
5. Delete Record
6. Search Records
7. Exit
""")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter choice (1-7): ")

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
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
