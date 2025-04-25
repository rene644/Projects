import sqlite3

conn = sqlite3.connect("call_center.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS calls (
    id INTEGER PRIMARY KEY,
    customer_name TEXT,
    phone TEXT,
    call_duration INTEGER
)
""")

conn.commit()
conn.close()
print("Table created successfully!")
