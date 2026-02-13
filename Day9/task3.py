# Demonstrate the handling of multiple possible input types in ERP (or)
# MES.
from dataclasses import dataclass
from typing import Union


@dataclass
class Transaction:
    item: str
    quantity: float 
    warehouse: str


def normalize_transaction(data: Union[dict, Transaction]) -> Transaction:
    if isinstance(data, Transaction):
        return data

    if isinstance(data, dict):
        return Transaction(
            item=data["item"],
            quantity=float(data["quantity"]),
            warehouse=data["warehouse"]
        )

    raise TypeError("Invalid transaction input")

print(normalize_transaction({"item": "item", "quantity": 1, "warehouse": "warehouse"}))