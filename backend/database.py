import sqlite3
from datetime import datetime

# Create database connection
conn = sqlite3.connect('data/soil_advisor.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS farmers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    village TEXT,
    registration_date TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS farms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_id INTEGER,
    farm_name TEXT,
    size_acres REAL,
    location TEXT,
    soil_type TEXT,
    FOREIGN KEY (farmer_id) REFERENCES farmers (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS soil_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farm_id INTEGER,
    reading_date TEXT,
    source TEXT,
    moisture REAL,
    ph REAL,
    soil_type TEXT,
    fertility_status TEXT,
    recommended_crops TEXT,
    fertilizer_advice TEXT,
    FOREIGN KEY (farm_id) REFERENCES farms (id)
)
''')

conn.commit()
conn.close()
print("Database created successfully!")