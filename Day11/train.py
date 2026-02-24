import logging
import sys
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

FEATURES = [
    "Ship Mode", "Segment", "Region",
    "Category", "Sub-Category",
    "Sales", "Quantity", "Discount"
]

CATEGORICAL_FEATURES = FEATURES[:5]
NUMERICAL_FEATURES = FEATURES[5:]

TARGET = "is_loss"
PROFIT_COL = "Profit"

DATA_PATH = "data/SampleSuperstore.csv"
MODEL_PATH = "model/loss_prediction_pipeline.pkl"

"""DEFINING FUNCTIONS"""

"""Reads the file , if the file is not found its lead to fail fast"""
def read_data(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except FileNotFoundError as e:
        logging.critical("Training file missing. Cannot proceed.")
        logging.critical(e)
        sys.exit(1)

"""Check for data validation"""
def validate_data(df: pd.DataFrame) -> None:
    if PROFIT_COL not in df.columns:
        raise ValueError("Profit column missing")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values")

"""Adds a new column to the dataframe"""
def add_feature(df: pd.DataFrame) -> pd.DataFrame:
    df[TARGET] = (df[PROFIT_COL] < 0).astype(int)
    return df

"""Splits Target and feature"""
def split_XY(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    X = df[FEATURES]
    y = df[TARGET]
    return X, y

"""Building pipline - Feature transformation"""
def build_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
            ("num", StandardScaler(), NUMERICAL_FEATURES),
        ]
    )

    pipeline = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])

    return pipeline



def main() -> None:
    logging.basicConfig(level=logging.INFO)

    # Load data
    df = read_data(DATA_PATH)

    # Validate before feature engineering
    validate_data(df)

    # Feature engineering
    df = add_feature(df)

    # Split features and target
    X, y = split_XY(df)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build pipeline
    pipeline = build_pipeline()

    # Train model
    pipeline.fit(X_train, y_train)

    # Evaluate
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(pipeline, MODEL_PATH)
    print("Model saved successfully!")

if __name__ == "__main__":
    main()