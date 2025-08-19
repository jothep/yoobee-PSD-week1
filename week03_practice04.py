from pathlib import Path
import sqlite3

DB_FILE = Path(__file__).resolve().parent / "data" / "users.db"

def init_db():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)  
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")      
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name  TEXT NOT NULL,
              email TEXT UNIQUE NOT NULL
            );
        """)
    return DB_FILE

def create_connection():
    conn = sqlite3.connect("data/users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")

def create_defined_table():
    conn = create_connection()
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CLASS (
            CLASS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CLASS_NAME TEXT NOT NULL,
            DESCRIPTION TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SUBJECTS (
            SUBJECT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SUBJECT_NAME TEXT NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LECTURER (
            LECTURER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LECTURER_NAME TEXT NOT NULL,
            SUBJECT_ID   INTEGER NOT NULL,
            FOREIGN KEY (SUBJECT_ID) REFERENCES SUBJECTS(SUBJECT_ID) ON UPDATE CASCADE  ON DELETE RESTRICT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STUDENT (
            STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            STUDENT_NAME TEXT NOT NULL,
            ADDRESS TEXT,
            CLASS_ID     INTEGER NOT NULL,
            FOREIGN KEY (CLASS_ID) REFERENCES CLASS(CLASS_ID)       ON UPDATE CASCADE   ON DELETE RESTRICT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STUDENTS_SUBJECTS (
            STUDENT_ID INTEGER NOT NULL,
            SUBJECT_ID INTEGER NOT NULL,
            PRIMARY KEY (STUDENT_ID, SUBJECT_ID),
            FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(STUDENT_ID) ON UPDATE CASCADE   ON DELETE RESTRICT,
            FOREIGN KEY (SUBJECT_ID) REFERENCES SUBJECTS(SUBJECT_ID) ON UPDATE CASCADE   ON DELETE RESTRICT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CLASS_SUBJECTS (
            CLASS_ID INTEGER NOT NULL,
            SUBJECT_ID INTEGER NOT NULL,
            PRIMARY KEY (CLASS_ID, SUBJECT_ID),
            FOREIGN KEY (CLASS_ID) REFERENCES CLASS(CLASS_ID) ON UPDATE CASCADE   ON DELETE RESTRICT,
            FOREIGN KEY (SUBJECT_ID) REFERENCES SUBJECTS(SUBJECT_ID) ON UPDATE CASCADE   ON DELETE RESTRICT
        )
    ''')
    
    conn.commit()
    conn.close()

def inspect_schema():
    conn = create_connection()
    cursor = conn.cursor()

    print("All tables:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for row in cursor.fetchall():
        print(row[0])
    conn.close()

def main():
    print("DB created at:", init_db())
    create_defined_table()
    inspect_schema()
    
if __name__ == "__main__":
    main()


