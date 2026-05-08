import pandas as pd
import os

# -----------------------------
# LOAD CSV SAFELY
# -----------------------------
def load_csv(path="data/expenses.csv"):
    """
    Loads expense CSV safely.
    If file not found → creates sample dataset.
    """

    if not os.path.exists(path):
        print("⚠️ No CSV found. Creating sample dataset...")

        sample = pd.DataFrame({
            "date": pd.date_range(start="2024-01-01", periods=10),
            "category": ["Food", "Travel", "Bills", "Shopping", "Food",
                         "Travel", "Bills", "Food", "Entertainment", "Other"],
            "amount": [-200, -500, -1000, -300, -150, -700, -1200, -100, -400, -250],
            "payment_method": ["UPI", "Card", "Cash", "UPI", "UPI",
                               "Card", "Cash", "UPI", "Card", "UPI"]
        })

        os.makedirs("data", exist_ok=True)
        sample.to_csv(path, index=False)

        return sample

    return pd.read_csv(path)