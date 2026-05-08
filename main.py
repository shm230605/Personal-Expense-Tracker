import pandas as pd
from src.visualization import (
    plot_category,
    plot_monthly,
    plot_daily,
    plot_payment,
    plot_summary
)

CSV_PATH = "data/expenses.csv"


def load_data():
    try:
        df = pd.read_csv(CSV_PATH)
    except FileNotFoundError:
        print("⚠️ CSV not found, creating sample data...")
        df = pd.DataFrame({
            "date": ["2025-01-01", "2025-01-02", "2025-01-03"],
            "category": ["income", "food", "shopping"],
            "amount": [60000, 2000, 3000],
            "payment": ["bank", "upi", "card"]
        })

    return df


def analyze(df):
    df.columns = df.columns.str.lower().str.strip()

    # safe defaults
    if "category" not in df.columns:
        df["category"] = "unknown"
    if "amount" not in df.columns:
        df["amount"] = 0

    df["category"] = df["category"].astype(str).str.lower().str.strip()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    income = df[df["category"] == "income"]["amount"].sum()
    spend = df[df["category"] != "income"]["amount"].sum()

    savings = float(income) - float(spend)

    return float(income), float(spend), float(savings), df


def main():
    print("\n💸 PERSONAL EXPENSE TRACKER SYSTEM\n")

    df = load_data()

    income, spend, savings, df = analyze(df)

    print("=" * 35)
    print(f"💰 TOTAL SPEND: ₹{spend:,.0f}")
    print(f"📈 INCOME: ₹{income:,.0f}")
    print(f"💾 SAVINGS: ₹{savings:,.0f}")
    print("=" * 35)

    print("\n📊 Generating charts...\n")

    plot_category(df)
    plot_monthly(df)
    plot_daily(df)
    plot_payment(df)
    plot_summary(income, spend, savings)

    print("\n✅ DONE — All charts generated safely!")


if __name__ == "__main__":
    main()