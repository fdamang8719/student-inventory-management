from inventory import items
from utils.helpers import (
    highest_stock_item,
    lowest_stock_item,
    average_stock,
    inventory_value,
)


def total_stock_value(items):
    """Calculate the total inventory value."""
    if not items:
        return 0
    return sum(inventory_value(item) for item in items)


def display_inventory():
    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("=" * 70)

    print(f"{'Item':<15}{'Qty':<10}{'Price($)':<15}{'Value($)':<15}")
    print("-" * 70)

    if not items:
        print("No inventory items available.")
        print("=" * 70)
        return

    for item in items:
        value = inventory_value(item)
        print(
            f"{item['item_name']:<15}"
            f"{item['quantity']:<10}"
            f"{item['price']:<15,.2f}"
            f"{value:<15,.2f}"
        )

    print("-" * 70)

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)

    print(f"Highest Stock Item : {highest['item_name']} ({highest['quantity']})")
    print(f"Lowest Stock Item  : {lowest['item_name']} ({lowest['quantity']})")
    print(f"Average Stock      : {average_stock(items):.2f}")
    print(f"Total Stock Value  : ${total_stock_value(items):,.2f}")

    print("=" * 70)


if __name__ == "__main__":
    display_inventory()