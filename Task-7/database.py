import sqlite3
from datetime import date

# Connect to the database
connection = sqlite3.connect("data/berry.db")
cursor = connection.cursor()


def create_user(user_id):
    cursor.execute("""
    INSERT OR IGNORE INTO users(user_id)
    VALUES(?)
    """, (user_id,))
    connection.commit()

def get_balance(user_id):
    cursor.execute("""
    SELECT berries
    FROM users
    WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()
    return result[0] if result else 0


def get_last_daily(user_id):
    cursor.execute("""
    SELECT last_daily
    FROM users
    WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()
    return result[0] if result else None


def update_daily(user_id, reward):
    cursor.execute("""
    UPDATE users
    SET
        berries = berries + ?,
        last_daily = ?
    WHERE user_id = ?
    """, (
        reward,
        str(date.today()),
        user_id
    ))

    connection.commit()


def trade_berries(sender_id, receiver_id, amount):

    cursor.execute("""
    UPDATE users
    SET berries = berries - ?
    WHERE user_id = ?
    """, (amount, sender_id))

    cursor.execute("""
    UPDATE users
    SET berries = berries + ?
    WHERE user_id = ?
    """, (amount, receiver_id))

    connection.commit()


def create_shop_tables():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shop(
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        price INTEGER,
        effect TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory(
        user_id INTEGER,
        item_id INTEGER,
        quantity INTEGER DEFAULT 0,
        PRIMARY KEY(user_id, item_id)
    )
    """)

    connection.commit()


def add_shop_items():

    items = [
        ("Den Den Mushi", 500, "A communication snail."),
        ("Meat", 150, "Luffy's favorite food."),
        ("Log Pose", 700, "Navigate the Grand Line."),
        ("Vivre Card", 1000, "A rare keepsake."),
        ("Cola", 250, "Franky's energy."),
        ("Beer", 350, "Pirate's pride.")
    ]

    cursor.executemany("""
    INSERT OR IGNORE INTO shop(name, price, effect)
    VALUES(?, ?, ?)
    """, items)

    connection.commit()


def get_shop_items():

    cursor.execute("""
    SELECT name, price, effect
    FROM shop
    """)

    return cursor.fetchall()

def get_item(item_name):

    cursor.execute("""
    SELECT item_id, name, price, effect
    FROM shop
    WHERE LOWER(name) = LOWER(?)
    """, (item_name,))

    return cursor.fetchone()


def remove_berries(user_id, amount):

    cursor.execute("""
    UPDATE users
    SET berries = berries - ?
    WHERE user_id = ?
    """, (amount, user_id))

    connection.commit()


def add_berries(user_id, amount):

    cursor.execute("""
    UPDATE users
    SET berries = berries + ?
    WHERE user_id = ?
    """, (amount, user_id))

    connection.commit()


def add_to_inventory(user_id, item_id):

    cursor.execute("""
    INSERT INTO inventory(user_id, item_id, quantity)
    VALUES(?, ?, 1)
    ON CONFLICT(user_id, item_id)
    DO UPDATE SET quantity = quantity + 1
    """, (user_id, item_id))

    connection.commit()



def get_inventory(user_id):

    cursor.execute("""
    SELECT shop.name,
           inventory.quantity
    FROM inventory
    INNER JOIN shop
        ON inventory.item_id = shop.item_id
    WHERE inventory.user_id = ?
    """, (user_id,))

    return cursor.fetchall()



def get_top_users():

    cursor.execute("""
    SELECT user_id, berries
    FROM users
    ORDER BY berries DESC
    LIMIT 5
    """)

    return cursor.fetchall()


def get_user_balance(user_id):
    return get_balance(user_id)