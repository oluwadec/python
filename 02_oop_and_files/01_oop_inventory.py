class InventoryItem:
    """Represents a single product item in an inventory system."""

    def __init__(self, item_id: str, name: str, price: float, quantity: int):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self) -> float:
        return round(self.price * self.quantity, 2)

    def restock(self, amount: int) -> None:
        if amount > 0:
            self.quantity += amount
            print(f" [+] Restocked {amount} units of '{self.name}'. New total: {self.quantity}")
        else:
            print(" [!] Restock amount must be greater than zero.")

    def sell(self, amount: int) -> bool:
        if amount <= 0:
            print(" [!] Sales amount must be greater than zero.")
            return False

        if amount <= self.quantity:
            self.quantity -= amount
            print(f" [-] Sold {amount} units of '{self.name}'. Remaining: {self.quantity}")
            return True
        else:
            print(f" [!] Insufficient stock for '{self.name}'. Available: {self.quantity}")
            return False

    def to_dict(self) -> dict:
        return {
            "id": self.item_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "total_value": self.calculate_total_value(),
        }


class Warehouse:
    """Manages a collection of InventoryItem objects using a dictionary."""

    def __init__(self, warehouse_name: str):
        self.warehouse_name = warehouse_name
        self.inventory = {}

    def add_item(self, item: InventoryItem) -> None:
        if item.item_id in self.inventory:
            print(f" [!] Item ID '{item.item_id}' already exists. Restocking existing item.")
            self.inventory[item.item_id].restock(item.quantity)
        else:
            self.inventory[item.item_id] = item
            print(f" [+] Added new item: '{item.name}' (ID: {item.item_id})")

    def get_total_inventory_value(self) -> float:
        total = 0.0
        for item in self.inventory.values():
            total += item.calculate_total_value()
        return round(total, 2)

    def display_report(self) -> None:
        print(f"\n========================================")
        print(f"  WAREHOUSE REPORT: {self.warehouse_name.upper()}")
        print(f"========================================")

        if not self.inventory:
            print(" No items in inventory.")
            return

        for item in self.inventory.values():
            info = item.to_dict()
            print(
                f" ID: {info['id']} | Name: {info['name']:<10} | Price: ${info['price']:<6.2f} | "
                f"Stock: {info['quantity']:<4} | Value: ${info['total_value']:.2f}"
            )

        print("----------------------------------------")
        print(f" TOTAL WAREHOUSE VALUE: ${self.get_total_inventory_value():.2f}")
        print("========================================\n")