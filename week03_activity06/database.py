import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "data" / "users.db"

def conn_db():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)  
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")      
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name  TEXT NOT NULL,
              email TEXT UNIQUE NOT NULL
            )
        """)
    return DB_FILE

def create_connection():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_FILE)

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

def create_yb_tables():
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

def view_all_tables():
    conn = create_connection()
    cursor = conn.cursor()
    rows = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]