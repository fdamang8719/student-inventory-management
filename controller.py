"""
controller.py

Controller layer for the Inventory Management System.
Handles communication between the application and the database.
"""

from models import InventoryItem
from database import get_inventory


def load_inventory():
    """
    Load inventory records from the database and convert them
    into InventoryItem objects.
    """

    rows = get_inventory()

    inventory = []

    for row in rows:
        item = InventoryItem(
            item_name=row[0],
            quantity=row[1],
            price=row[2]
        )

        inventory.append(item)

    return inventory


def total_inventory_value(items):
    """
    Calculate the total value of all inventory items.
    """

    return sum(item.total_value() for item in items)


def highest_stock_item(items):
    """
    Return the item with the highest stock quantity.
    """

    return max(items, key=lambda item: item.quantity)


def lowest_stock_item(items):
    """
    Return the item with the lowest stock quantity.
    """

    return min(items, key=lambda item: item.quantity)