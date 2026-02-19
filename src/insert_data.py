import sqlite3

conn = sqlite3.connect("data/study.db")
cursor = conn.cursor()

data = [
    ("Operating Systems", 60, "2026-02-18"),
    ("DSA Practice", 45, "2026-02-18"),
    ("Networks", 30, "2026-02-17"),
    ("Operating Systems", 40, "2026-02-17"),
]

cursor.executemany(
    "INSERT INTO study_sessions (topic, duration, date) VALUES (?, ?, ?)",
    data
)

conn.commit()
conn.close()

print("Data inserted!")
