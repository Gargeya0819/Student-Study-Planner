import sqlite3

conn = sqlite3.connect("studyplanner.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    difficulty INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    task_name TEXT,
    deadline TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
