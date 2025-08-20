from database import create_connection
import sqlite3

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

def add_record_generic(table):
    conn = create_connection()
    cols = conn.execute(f"PRAGMA table_info({table})").fetchall()
    insert_cols, insert_vals = [], []

    for (cid, name, ctype, notnull, dflt_value, pk) in cols:
        if pk and str(ctype).upper().startswith("INTEGER"):
            continue

        prompt = f"{name} ({ctype}{' NOT NULL' if notnull else ''}"
        if dflt_value is not None:
            prompt += f", DEFAULT={dflt_value}"
        prompt += "): "

        while True:
            raw = input(prompt)
            if raw == "":
                if notnull and dflt_value is None:
                    print("This Col is NOT NULL and NO Default, please input")
                    continue
                if dflt_value is None:
                    insert_cols.append(name)
                    insert_vals.append(None)
                break
            insert_cols.append(name)
            insert_vals.append(raw)
            break

    if insert_cols:
        ph = ",".join("?" for _ in insert_cols)
        col_list = ",".join(insert_cols)
        sql = f"INSERT INTO {table} ({col_list}) VALUES ({ph})"
        conn.execute(sql, insert_vals)
    else:
        conn.execute(f"INSERT INTO {table} DEFAULT VALUES")

    conn.commit()
    print("✔ Inserted.")

def delete_one_record(table):
    conn = create_connection()
    rid = input("Enter rowid to delete: ").strip()
    cur = conn.execute(f"DELETE FROM {table} WHERE rowid = ?", (rid,))
    conn.commit()
    print("\n🗑️ Deleted rows:", cur.rowcount)
    conn.close()

def list_contents(table):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return rows