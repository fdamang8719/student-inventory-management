"""
app.py

Main application for the Inventory Management System.
"""

from database import create_database, insert_sample_data
from controller import (
    load_inventory,
    total_inventory_value,
    highest_stock_item,
    lowest_stock_item,
)

LINE_WIDTH = 75


def display_inventory():
    """Display all inventory records and summary statistics."""

    # Create database and populate it with sample data (only once)
    create_database()
    insert_sample_data()

    # Load inventory from the database
    items = load_inventory()

    print("\n")
    print("=" * LINE_WIDTH)
    print("               INVENTORY MANAGEMENT SYSTEM")
    print("=" * LINE_WIDTH)

    print(f"{'Item':<15}{'Qty':<10}{'Price($)':<15}{'Value($)':<15}")
    print("-" * LINE_WIDTH)

    if not items:
        print("No inventory items available.")
        print("=" * LINE_WIDTH)
        return

    # Display inventory items
    for item in items:
        print(
            f"{item.item_name:<15}"
            f"{item.quantity:<10}"
            f"{item.price:<15,.2f}"
            f"{item.total_value():<15,.2f}"
        )

    print("-" * LINE_WIDTH)

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)

    print(f"Highest Stock Item      : {highest.item_name} ({highest.quantity})")
    print(f"Lowest Stock Item       : {lowest.item_name} ({lowest.quantity})")
    print(f"Total Inventory Items   : {len(items)}")
    print(f"Total Stock Value       : ${total_inventory_value(items):,.2f}")

    print("=" * LINE_WIDTH)


if __name__ == "__main__":
    display_inventory()