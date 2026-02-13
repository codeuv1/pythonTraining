# Write a function to calculate the shipment weight of warehouse.
#
# Input– (weight per unit, Quantity)
# Provide 3 testcases to demonstrate function annotations and return types.
# Let one testcase be typed wrongly (type error). observe it in mypy.

def calculate_shipment_weight(weight_per_unit:float , quantity:int)->float:
    return weight_per_unit * quantity

print(calculate_shipment_weight(100,10))
print(calculate_shipment_weight(12.3,10))
print(calculate_shipment_weight("abc",10)) #wrong

