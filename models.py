"""
models.py

Defines the InventoryItem class used throughout the application.
"""

class InventoryItem:
    """Represents a single inventory item."""

    def __init__(self, item_name: str, quantity: int, price: float):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def total_value(self) -> float:
        """Returns the total value of this inventory item."""
        return self.quantity * self.price