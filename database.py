"""
database.py

Creates and manages the SQLite database for the Inventory Management System.
"""
import os
import sqlite3

DATABASE_NAME = os.path.join("data", "inventory.db")

import sqlite3

DATABASE_NAME = "inventory.db"


def create_database():
    """Creates the inventory database and table if they do not exist."""

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_sample_data():
    """Inserts sample inventory records if the table is empty."""

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM inventory")
    count = cursor.fetchone()[0]

    if count == 0:
        items = [
            ("Laptop", 5, 850.00),
            ("Mouse", 20, 15.50),
            ("Keyboard", 12, 30.00),
            ("Monitor", 8, 220.00),
            ("Printer", 4, 150.00)
        ]

        cursor.executemany(
            "INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)",
            items
        )

    conn.commit()
    conn.close()


def get_inventory():
    """Returns all inventory records."""

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT item_name, quantity, price FROM inventory")

    rows = cursor.fetchall()

    conn.close()

    return rows