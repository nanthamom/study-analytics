import sqlite3

conn = sqlite3.connect("data/study.db")
cursor = conn.cursor()

data = [
    ("Operating Systems", 60, "2026-02-18", 4),
    ("DSA Practice", 45, "2026-02-18", 5),
    ("Networks", 30, "2026-02-17", 3),
    ("Operating Systems", 40, "2026-02-17", 4),
]

cursor.executemany(
    "INSERT INTO study_sessions (topic, duration, date, difficulty) VALUES (?, ?, ?, ?)",
    data
)

conn.commit()
conn.close()

print("Data inserted!")
