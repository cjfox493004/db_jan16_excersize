import sqlite3

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()
query = """
INSERT INTO points (City, Name)
VALUES
("Seattle","Seahawks"),
("New England","Patriots"),
("Denver","Broncos"),
("Los Angeles","Rams"),
("Buffalo","Bills"),
("Houston","Texans"),
("Chicago","Bears"),
("San Francisco","49ers")
"""
cursor.execute(query)
conn.commit()
conn.close()