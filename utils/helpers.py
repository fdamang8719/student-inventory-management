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