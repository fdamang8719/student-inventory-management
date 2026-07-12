"""Helper functions for the Inventory Management System."""

from typing import List, Dict, Optional


def inventory_value(item: Dict) -> float:
    """Return the total value of an inventory item."""
    return item["quantity"] * item["price"]


def highest_stock_item(items: List[Dict]) -> Optional[Dict]:
    """Return the item with the highest quantity."""
    if not items:
        return None
    return max(items, key=lambda item: item["quantity"])


def lowest_stock_item(items: List[Dict]) -> Optional[Dict]:
    """Return the item with the lowest quantity."""
    if not items:
        return None
    return min(items, key=lambda item: item["quantity"])


def average_stock(items: List[Dict]) -> float:
    """Return the average stock quantity."""
    if not items:
        return 0

    return sum(item["quantity"] for item in items) / len(items)


def most_valuable_item(items: List[Dict]) -> Optional[Dict]:
    """Return the inventory item with the highest total value."""
    if not items:
        return None

    return max(items, key=inventory_value)


def least_valuable_item(items: List[Dict]) -> Optional[Dict]:
    """Return the inventory item with the lowest total value."""
    if not items:
        return None

    return min(items, key=inventory_value)


def average_inventory_value(items: List[Dict]) -> float:
    """Return the average inventory value."""
    if not items:
        return 0

    return sum(inventory_value(item) for item in items) / len(items)