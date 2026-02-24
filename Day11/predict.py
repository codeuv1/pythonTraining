import joblib
import pandas as pd
from typehints import Order


def predict_order(order_dict:Order):
    try:
        model = joblib.load("model/loss_prediction_pipeline.pkl")
        input_df = pd.DataFrame([order_dict])
        prediction = model.predict(input_df)
        return {"is_loss": int(prediction[0]), "status": "main_model"}

    except Exception as e:
        print("Prediction failed:", e)
        return {"is_loss": None, "status": "fallback_safe"}

if __name__ == "__main__":
    valid_order = {
        "Ship Mode": "Standard Class",
        "Segment": "Consumer",
        "Region": "West",
        "Category": "Technology",
        "Sub-Category": "Phones",
        "Sales": 500,
        "Quantity": 3,
        "Discount": 0.1
    }

    invalid_order = {
    "Ship Mode": "Standard Class",
        "Segment": "Consumer",
        "Region": "West",
        "Category": "Technology",
        "Sub-Category": "Phones",
        "Sales": 500,
        "Quantity": 3,
    }
    print(predict_order(valid_order))
    print(predict_order(invalid_order))
