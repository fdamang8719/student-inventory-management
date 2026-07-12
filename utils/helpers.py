def highest_stock_item(items):
    """Return the item with the highest quantity."""
    if not items:
        return None
    return max(items, key=lambda item: item["quantity"])


def lowest_stock_item(items):
    """Return the item with the lowest quantity."""
    if not items:
        return None
    return min(items, key=lambda item: item["quantity"])


def average_stock(items):
    """Return the average stock quantity."""
    if not items:
        return 0
    total = sum(item["quantity"] for item in items)
    return total / len(items)

def inventory_value(item):
    """Return the total value of an inventory item."""
    return item["quantity"] * item["price"]
def inventory_value(item):
    """Return the total value of an inventory item."""
    return item["quantity"] * item["price"]

def most_valuable_item(items):
    """Return the inventory item with the highest total value."""
    if not items:
        return None
    return max(items, key=lambda item: item["quantity"] * item["price"])


def least_valuable_item(items):
    """Return the inventory item with the lowest total value."""
    if not items:
        return None
    return min(items, key=lambda item: item["quantity"] * item["price"])


def average_inventory_value(items):
    """Return the average inventory value."""
    if not items:
        return 0

    total = sum(item["quantity"] * item["price"] for item in items)
    return total / len(items)