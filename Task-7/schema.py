from database import connection, cursor

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    berries INTEGER DEFAULT 500,
    last_daily TEXT
)
""")

connection.commit()