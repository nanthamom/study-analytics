# Study Analytics System

A lightweight data analytics project that tracks and analyses personal study sessions using Python, SQLite, and SQL.

# Features
- Store study sessions in a SQLite database
- Analyse total study time per topic
- Compute average session length
- Identify most studied subjects
- Query data using SQL

# Tech Stack
- Python 3
- SQLite
- SQL (aggregation, grouping, filtering)
- DataGrip (for visual database exploration)

# Project Structure

study-analytics/
│
├── data/
│ └── study.db
│
├── src/
│ ├── create_db.py
│ ├── insert_data.py
│ └── analysis.py
│
└── README.md


# How It Works
1. Create database:
2. Insert sample data: python3 src/insert_data.py
3. Run analysis: python3 src/analysis.py

# Example SQL Query 

SELECT topic, SUM(duration) AS total_minutes
FROM study_sessions
GROUP BY topic
ORDER BY total_minutes DESC;

# Example OUTPUT 

Operating Systems - 100 minutes
DSA Practice - 45 minutes
Networks - 30 minutes

# What I Learned from Mini Project 

- Designing a Relational Database Schema
- Wrting SQL Queries with GROUP BY and aggregation
- Connecting Python Applications to Database
- Using DataGrip to inspect and query data

# Work in Progress Improvements 

- Add Difficulty/Focus Score Tracking
- Visualise Data Using Matplotlib 
- Build a CLI Interface for Inserting Sessions
- Integrated with a C++ Tracker Application 

# Visualisation 

[Study Time Chart] (study_chart.png)

Total study time: 175 minutes  
Most studied topic: Operating Systems - 100 minutes  
Average session: 43.75 minutes  

Average difficulty per topic:
DSA Practice - 5.0  
Networks - 3.0  
Operating Systems - 4.0  

# Author 

Nantha, M.
2nd-Year CS Student Building Data-Driven Systems. 