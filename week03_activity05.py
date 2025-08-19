from pathlib import Path
import sqlite3

DB_FILE = Path(__file__).resolve().parent / "data" / "users.db"

def create_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def create_table_students():
    conn = create_connection()
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            Stu_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Stu_name TEXT NOT NULL,
            Stu_address TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Students (Stu_name, Stu_address) VALUES ('JSK', '12 Sunset Rd');
    ''')
    cursor.execute('''
        INSERT INTO Students (Stu_name, Stu_address) VALUES ('Jothep', '2A Queen St')
    ''')
    
    conn.commit()
    conn.close()

def show_users_and_students():
    conn = create_connection()
    cursor = conn.cursor()

    users = cursor.execute("SELECT id, name, email FROM users;").fetchall()
    print(*users, sep="\n") if users else print("(empty)")

    print("=== Students ===")
    students = cursor.execute("SELECT Stu_ID, Stu_name, Stu_address FROM Students;").fetchall()
    print(students)
    print(*students, sep="\n") if students else print("(empty)")
    conn.close()

def main():
    create_table_students()
    show_users_and_students()
    
if __name__ == "__main__":
    main()
