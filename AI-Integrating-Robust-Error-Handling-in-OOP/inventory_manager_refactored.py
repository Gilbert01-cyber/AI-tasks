class InvalidProductDataError(Exception):
    """Custom exception raised when Product data fails validation."""
    pass


class Product:
    """Represents a product with a name, price, and quantity."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        """Return the price of the product."""
        return self._price

    @price.setter
    def price(self, value):
        """Validate and set the price of the product."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise InvalidProductDataError(
                "Price must be a number, got {}".format(type(value).__name__)
            )
        if value < 0:
            raise InvalidProductDataError(
                "Price cannot be negative, got {}".format(value)
            )
        self._price = value

    @property
    def quantity(self):
        """Return the quantity of the product."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Validate and set the quantity of the product."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise InvalidProductDataError(
                "Quantity must be an integer, got {}".format(type(value).__name__)
            )
        if value < 0:
            raise InvalidProductDataError(
                "Quantity cannot be negative, got {}".format(value)
            )
        self._quantity = value


class InventoryManager:
    """Manages the collection of products and provides inventory operations."""

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add_product(self, product):
        """Adds a product object to the inventory list."""
        self.inventory.append(product)

    def update_quantity(self, name, new_quantity):
        """Updates the quantity of a product by name."""
