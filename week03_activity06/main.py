from database import conn_db, create_yb_tables, view_all_tables
from user_manager import add_user, view_users, search_user, delete_user, add_record_generic, list_contents, delete_one_record

def table_menu():
    print("\n==== Table Manager ====")
    print("1. Add Tables of YB College")
    print("2. View All Tables")
    print("3. Select a Table to Manage")
    print("4. Manage Table users")
    print("5. Exit")

def manage_table_menu():
    print("\n==== Selected Table Manager ====")
    print("1. Add record")
    print("2. Delete record")
    print("3. View All records of Table")
    print("4. Return to last menu")

def users_menu():
    print("\n==== User Table Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Return to last menu")


def table_menu_loop():
    conn_db()
    while True:
        table_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            create_yb_tables()
            print("\nYB College Tables created.")
        elif choice == "2":
            tables = view_all_tables()
            print("\nAll tables:", ", ".join(tables) if tables else "(none)")
        elif choice == "3":
            tables = view_all_tables()
            print("\nAll tables:", ", ".join(tables) if tables else "(none)")
            t = input("Enter table name: ").strip()
            if t in tables:
                manage_table_menu_loop(t)
            else:
                print("\nNo such table.")
        elif choice == "4":
            users_menu_loop()
        else:
            print("\nGoodbye!")
            break

def manage_table_menu_loop(table):
    conn_db()
    while True:
        manage_table_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_record_generic(table)
        elif choice == "2":
            delete_one_record(table)
        elif choice == "3":
            rows = list_contents(table)
            if not rows:
                print("(empty)")
            else:
                for r in rows:
                    print("\n", r)
        else:
            return

def users_menu_loop():
    conn_db()
    while True:
        users_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print("\n", user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print("\n", user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice, try again.")

def main():
    table_menu_loop()

if __name__ == "__main__":
    main()
