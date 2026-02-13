from typing import TypeVar

T = TypeVar('T')

class Vendor:
    def __init__(self, id: str ,name: str) -> None:
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return f'Vendors(id={self.id}, name={self.name})'

class VendorsRepository:
    def __init__(self) -> None:
        self.vendors = []

    def add(self, vendor: Vendor) -> None:
        self.vendors.append(vendor)

    def extend(self, vendors: list[Vendor]) -> None:
        self.vendors.extend(vendors)

    def remove(self, vendor: Vendor) -> None:
        self.vendors.remove(vendor)


vendorsRepository = VendorsRepository()

ven1 = vendorsRepository.add(Vendor('Ven1','Ven1'))
ven2 = vendorsRepository.add(Vendor('Ven2','Ven2'))
ven3 = vendorsRepository.add(Vendor('Ven3','Ven3'))

print(vendorsRepository.vendors)



