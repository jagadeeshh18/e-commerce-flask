import sqlite3
def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id integer primary key autoincrement,
            username text,
            mobile text,
            password text)""")
    conn.commit()
    conn.close()