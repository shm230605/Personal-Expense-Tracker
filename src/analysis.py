import pandas as pd

def analyze_data(df):
    df = df.copy()

    # normalize columns
    df.columns = [c.lower() for c in df.columns]

    income = 0
    expense = 0

    # CASE 1: if type column exists
    if "type" in df.columns:
        df["type"] = df["type"].str.lower()

        income = df[df["type"] == "income"]["amount"].sum()
        expense = df[df["type"] == "expense"]["amount"].sum()

    # CASE 2: fallback logic
    else:
        income = df[df["amount"] > 0]["amount"].sum()
        expense = abs(df[df["amount"] < 0]["amount"].sum())

    savings = income - expense

    return {
        "income": round(float(income), 2),
        "total_expense": round(float(expense), 2),
        "savings": round(float(savings), 2)
    }