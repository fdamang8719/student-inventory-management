from inventory import items
from utils.helpers import (
    highest_stock_item,
    lowest_stock_item,
    average_stock,
    inventory_value,
    most_valuable_item,
    least_valuable_item,
    average_inventory_value,
)


def total_stock_value(items):
    """Calculate total inventory value."""
    if not items:
        return 0

    return sum(inventory_value(item) for item in items)


def display_inventory():

    print("\n")
    print("=" * 75)
    print("             INVENTORY MANAGEMENT SYSTEM")
    print("=" * 75)

    print(f"{'Item':<15}{'Qty':<10}{'Price($)':<15}{'Value($)':<15}")
    print("-" * 75)

    if not items:
        print("No inventory items available.")
        print("=" * 75)
        return

    for item in items:
        value = inventory_value(item)

        print(
            f"{item['item_name']:<15}"
            f"{item['quantity']:<10}"
            f"{item['price']:<15,.2f}"
            f"{value:<15,.2f}"
        )

    print("-" * 75)

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    most_value = most_valuable_item(items)
    least_value = least_valuable_item(items)

    print(f"Highest Stock Item     : {highest['item_name']} ({highest['quantity']})")
    print(f"Lowest Stock Item      : {lowest['item_name']} ({lowest['quantity']})")
    print(f"Most Valuable Item     : {most_value['item_name']}")
    print(f"Least Valuable Item    : {least_value['item_name']}")
    print(f"Average Stock          : {average_stock(items):.2f}")
    print(f"Average Inventory Value: ${average_inventory_value(items):,.2f}")
    print(f"Total Inventory Items  : {len(items)}")
    print(f"Total Stock Value      : ${total_stock_value(items):,.2f}")

    print("=" * 75)


if __name__ == "__main__":
    display_inventory()