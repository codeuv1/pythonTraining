from typing import TypedDict

class Order(TypedDict):
    Ship_Mode: str
    Segment: str
    Region: str
    Category: str
    Sub_Category: str
    Sales: int
    Quantity: int
    Discount: float