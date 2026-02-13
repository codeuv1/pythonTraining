# Write a simple function incorporating OPTIONAL for ERP System.

from typing import Optional
from typing import TypedDict

class Supplier(TypedDict):
    name: str
    rating: float | int
    city: str

supplier_list: dict[str, Supplier] = {
    "ID001" : {'name' : 'Super Suppliers',
               'rating' : 4,
               'city':'Delhi'},
    "ID002" : {'name' : 'Adani Supply',
               'rating' : 4.3,
               'city':'Bangalore'},
    "ID003" : {'name' : 'Reliance Ports',
               'rating' : 4.4,
               'city':'Surat'},
}

def get_supplier_info(id : str , supplier_list : dict[str,Supplier]) -> Optional[Supplier]:
    return supplier_list[id] if id in supplier_list else None

print(get_supplier_info("ID001",supplier_list))
print(get_supplier_info("ID002",supplier_list))
