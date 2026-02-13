
# Develop a snippet comprising of any one of the following ERP Domain
# Models using custom classes.
# Vendor, Product, Purchase Item, Purchase Order, Inventory

from typing import Union
class Product:
    def __init__(self, sku: str, name: str):
        if not isinstance(sku, str):
            raise TypeError("SKU must be a string")
        if not isinstance(name, str):
            raise TypeError("Product name must be a string")

        self.sku = sku
        self.name = name

class Inventory:
    def __init__(self, product: Product, warehouse: str, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("product must be of type Product")

        if not isinstance(warehouse, str):
            raise TypeError("warehouse must be a string")

        if not isinstance(quantity, int):
            raise TypeError("quantity must be numeric")

        if quantity < 0:
            raise ValueError("Initial quantity cannot be negative")

        self.product = product
        self.warehouse = warehouse
        self.quantity = float(quantity)


    def stock_in(self, amount: Union[int, float]) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Stock in amount must be numeric")

        if amount <= 0:
            raise ValueError("Stock in amount must be positive")

        self.quantity += amount

    def stock_out(self, amount: Union[int, float]) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Stock out amount must be numeric")

        if amount <= 0:
            raise ValueError("Stock out amount must be positive")

        if amount > self.quantity:
            raise ValueError("Insufficient stock")

        self.quantity -= amount


product = Product("BIS001", "Chocolate Biscuit")

inventory = Inventory(product, "W01", 100)

inventory.stock_in(50)
inventory.stock_out(30)

print(inventory.quantity)
