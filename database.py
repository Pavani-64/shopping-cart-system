import sqlite3

DB_NAME = "shop.db"


def connect():
    return sqlite3.connect(DB_NAME)


# ---------- CREATE TABLES ----------
def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        product_name TEXT,
        price REAL,
        quantity INTEGER
    )
    """)

    conn.commit()
    conn.close()


# ---------- USER ----------
def add_user(username, password):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
    except:
        return False

    conn.close()
    return True


def check_user(username, password):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user is not None


# ---------- CART ----------
def add_to_cart(username, name, price, qty):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cart (username, product_name, price, quantity) VALUES (?, ?, ?, ?)",
        (username, name, price, qty)
    )

    conn.commit()
    conn.close()


def get_cart(username):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT product_name, price, quantity FROM cart WHERE username=?",
        (username,)
    )

    items = cursor.fetchall()
    conn.close()

    return items


# ---------- REMOVE ----------
def remove_item(username, product_name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM cart WHERE username=? AND product_name=?",
        (username, product_name)
    )

    conn.commit()
    conn.close()


# ---------- CLEAR CART ----------
def clear_cart(username):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM cart WHERE username=?",
        (username,)
    )

    conn.commit()
    conn.close()