from statistics import mean

# Forecasting
def forecast_demand(demand_history, window=3):
    if len(demand_history) < window:
        raise ValueError("Insufficient demand history")
    return int(mean(demand_history[-window:]))

# Planning
def plan_quantity(forecast, safety_stock):
    return forecast + safety_stock

def calculate_order_quantity(planned_qty, warehouse_stock):
    return max(planned_qty - warehouse_stock, 0)

#supplier
def select_supplier(order_qty, suppliers):
    eligible_suppliers = [s for s in suppliers if s["capacity"] >= order_qty]
    if not eligible_suppliers:
        raise RuntimeError("No supplier can fulfill order")

    return min(eligible_suppliers, key=lambda s: s["unit_cost"])

# Cost & Approval
def calculate_cost(order_qty, unit_cost):
    return order_qty * unit_cost


def approve_budget(total_cost, company_budget):
    return total_cost <= company_budget

def run_pipeline(
    demand_history,
    warehouse_stock,
    suppliers,
    safety_stock,
    company_budget,
):
    forecast = forecast_demand(demand_history)
    planned_qty = plan_quantity(forecast, safety_stock)
    order_qty = calculate_order_quantity(planned_qty, warehouse_stock)

    if order_qty == 0:
        return {
            "order_required": False,
            "reason": "Sufficient warehouse stock",
            "forecasted_demand": forecast,

            "order_quantity": order_qty,
            "supplier": None,
            "total_cost": 0,
            "approved": False,
        }

    supplier = select_supplier(order_qty, suppliers)
    total_cost = calculate_cost(order_qty, supplier["unit_cost"])
    approved = approve_budget(total_cost, company_budget)

    return {
        "forecasted_demand" : forecast,
        "order_required": True,
        "order_quantity": order_qty,
        "supplier": supplier["name"],
        "total_cost": total_cost,
        "approved": approved,
    }



def main():
    demand_history = [120, 100, 500, 450, 380,10,18,56]
    warehouse_stock = 200
    safety_stock = 50
    company_budget = 5000

    suppliers = [
        {"name": "Supplier_A", "unit_cost": 10, "capacity": 300},
        {"name": "Supplier_B", "unit_cost": 9, "capacity": 500},
    ]

    result = run_pipeline(
        demand_history=demand_history,
        warehouse_stock=warehouse_stock,
        suppliers=suppliers,
        safety_stock=safety_stock,
        company_budget=company_budget,
    )

    if not result["order_required"]:
        print("No order required:", result["reason"])
        return
    else:
        print(result['forecasted_demand'])
        print(
            f"Order {result['order_quantity']} units from {result['supplier']} | "
            f"Cost: {result['total_cost']} | Approved: {result['approved']}"
        )


if __name__ == "__main__":
    main()
