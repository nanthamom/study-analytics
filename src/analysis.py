import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/study.db")
cursor = conn.cursor()

# total study time
cursor.execute("SELECT SUM(duration) FROM study_sessions")
total = cursor.fetchone()[0]
print("Total study time:", total, "minutes")

# most studied topic
cursor.execute("""
SELECT topic, SUM(duration)
FROM study_sessions
GROUP BY topic
ORDER BY SUM(duration) DESC
LIMIT 1
""")
top = cursor.fetchone()
print("Most studied topic:", top[0], "-", top[1], "minutes")

# average session length
cursor.execute("SELECT AVG(duration) FROM study_sessions")
avg = cursor.fetchone()[0]
print("Average session:", round(avg, 2), "minutes")

# average difficulty per topic
cursor.execute("""
SELECT topic, AVG(difficulty)
FROM study_sessions
GROUP BY topic
""")

print("\nAverage difficulty per topic:")
for row in cursor.fetchall():
    print(row[0], "-", round(row[1], 2))

# chart
cursor.execute("""
SELECT topic, SUM(duration)
FROM study_sessions
GROUP BY topic
""")

data = cursor.fetchall()
topics = [row[0] for row in data]
durations = [row[1] for row in data]

plt.bar(topics, durations)
plt.title("Study Time per Topic")
plt.xlabel("Topic")
plt.ylabel("Minutes")
plt.show()

plt.savefig("study_chart.png")

# CLOSE CONNECTION AT THE VERY END
conn.close()
