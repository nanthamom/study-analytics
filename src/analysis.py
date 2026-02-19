import sqlite3

conn = sqlite3.connect("data/study.db")
cursor = conn.cursor()

# total study time
cursor.execute("SELECT SUM(duration) FROM study_sessions")
total = cursor.fetchone()[0]
print("Total study time:", total, "minutes")

# most studied topic
cursor.execute("""
SELECT topic, SUM(duration) as total_time
FROM study_sessions
GROUP BY topic
ORDER BY total_time DESC
LIMIT 1
""")

top = cursor.fetchone()
print("Most studied topic:", top[0], "-", top[1], "minutes")

# average session length
cursor.execute("SELECT AVG(duration) FROM study_sessions")
avg = cursor.fetchone()[0]
print("Average session:", avg, "minutes")

conn.close()
