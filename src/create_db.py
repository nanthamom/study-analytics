import sqlite3

conn = sqlite3.connect("data/study.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS study_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    duration INTEGER,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Database created!")
