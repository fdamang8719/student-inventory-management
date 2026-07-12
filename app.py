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

# Constant used for formatting the output
LINE_WIDTH = 75


def total_stock_value(items):
    """
    Calculate the total value of all inventory items.
    """
    if not items:
        return 0

    return sum(inventory_value(item) for item in items)


def display_inventory():
    """
    Display the inventory records and summary statistics.
    """

    print("\n")
    print("=" * LINE_WIDTH)
    print("               INVENTORY MANAGEMENT SYSTEM")
    print("=" * LINE_WIDTH)

    print(f"{'Item':<15}{'Qty':<10}{'Price($)':<15}{'Value($)':<15}")
    print("-" * LINE_WIDTH)

    # Handle empty inventory
    if not items:
        print("No inventory items available.")
        print("=" * LINE_WIDTH)
        return

    # Display inventory items
    for item in items:
        value = inventory_value(item)

        print(
            f"{item['item_name']:<15}"
            f"{item['quantity']:<10}"
            f"{item['price']:<15,.2f}"
            f"{value:<15,.2f}"
        )

    print("-" * LINE_WIDTH)

    # Calculate statistics
    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    most_value = most_valuable_item(items)
    least_value = least_valuable_item(items)

    # Display summary
    print(f"Highest Stock Item      : {highest['item_name']} ({highest['quantity']})")
    print(f"Lowest Stock Item       : {lowest['item_name']} ({lowest['quantity']})")
    print(f"Most Valuable Item      : {most_value['item_name']}")
    print(f"Least Valuable Item     : {least_value['item_name']}")
    print(f"Average Stock           : {average_stock(items):.2f}")
    print(f"Average Inventory Value : ${average_inventory_value(items):,.2f}")
    print(f"Total Inventory Items   : {len(items)}")
    print(f"Total Stock Value       : ${total_stock_value(items):,.2f}")

    print("=" * LINE_WIDTH)


if __name__ == "__main__":
    display_inventory()