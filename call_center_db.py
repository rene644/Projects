import sqlite3
import pandas as pd

data = {
    'Call ID': [1, 2, 3, 4, 5],
    'Agent': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Duration (minutes)': [5, 10, 7, 12, 8],
    'Customer Satisfaction': [4, 5, 3, 5, 4],
    'Call Type': ['Inquiry', 'Complaint', 'Inquiry', 'Sales', 'Complaint']
}

df = pd.DataFrame(data)

conn = sqlite3.connect('call_center.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS calls (
        id INTEGER PRIMARY KEY,
        agent TEXT,
        duration INTEGER,
        satisfaction INTEGER,
        call_type TEXT
    )
''')

# Insert data
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO calls (agent, duration, satisfaction, call_type)
        VALUES (?, ?, ?, ?)
    ''', (row['Agent'], row['Duration (minutes)'], row['Customer Satisfaction'], row['Call Type']))

conn.commit()
conn.close()

conn = sqlite3.connect('call_center.db')  # Corrected variable name
cursor = conn.cursor()

cursor.execute('SELECT * FROM calls WHERE duration > 8')
rows = cursor.fetchall()

for row in rows:
    print(row)  # Indented line

cursor.execute('SELECT * FROM calls WHERE agent = "Alice"')
rows = cursor.fetchall()

cursor.execute('SELECT AVG(duration) FROM calls')
average_duration = cursor.fetchone()[0]
print(average_duration)

for row in rows:
    print(row)

conn.close()