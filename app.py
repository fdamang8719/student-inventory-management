from inventory import items
from utils.helpers import (
    highest_stock_item,
    lowest_stock_item,
    average_stock,
)


def total_stock_value(items):
    """Calculate total inventory value."""
    return sum(item["quantity"] * item["price"] for item in items)


def display_inventory():
    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("=" * 55)

    print(f"{'Item':<15}{'Qty':<10}{'Price($)':<12}{'Value($)'}")
    print("-" * 55)

    for item in items:
        value = item["quantity"] * item["price"]
        print(f"{item['item_name']:<15}{item['quantity']:<10}{item['price']:<12}{value}")

    print("-" * 55)

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)

    print(f"Highest Stock Item : {highest['item_name']} ({highest['quantity']})")
    print(f"Lowest Stock Item  : {lowest['item_name']} ({lowest['quantity']})")
    print(f"Average Stock      : {average_stock(items):.2f}")
    print(f"Total Stock Value  : ${total_stock_value(items):,.2f}")

    print("=" * 55)


if __name__ == "__main__":
    display_inventory()