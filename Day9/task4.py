# 4. Write a snippet to demonstrate the use of dict typing in ERP.

from typing import TypedDict


class InventoryTransaction(TypedDict):
    item_code: str
    quantity: float
    warehouse: str
    movement_type: str

def process_inventory(txn: InventoryTransaction) -> None:
    if txn["movement_type"] == "IN":
        print(f"Adding {txn['quantity']} units of {txn['item_code']} to {txn['warehouse']}")

    elif txn["movement_type"] == "OUT":
        print(f"Removing {txn['quantity']} units of {txn['item_code']} from {txn['warehouse']}")

    else:
        raise ValueError("Invalid movement type")

transaction_data: InventoryTransaction = {
    "item_code": "BIS001",
    "quantity": 100,
    "warehouse": "W01",
    "movement_type": "OUT"
}

process_inventory(transaction_data)
