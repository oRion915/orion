from core.storage import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
connection.close()

print("Database initialized successfully!")
