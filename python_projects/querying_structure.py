import sqlite3

conn = sqlite3.connect("call_center.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Check sample data from each table
for table in tables:
    cursor.execute(f"SELECT * FROM {table[0]} LIMIT 5;")
    print(f"\nContents of {table[0]}:")
    print(cursor.fetchall())

conn.close()
