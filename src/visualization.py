import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = "outputs/charts"


# ✅ MUST exist (fixes your import error)
def ensure_environment():
    os.makedirs(BASE_DIR, exist_ok=True)


# auto-create folder when module loads
ensure_environment()


def get_path(filename):
    ensure_environment()
    return os.path.join(BASE_DIR, filename)


# ---------------- CATEGORY ----------------
def plot_category(df):
    if df is None or df.empty:
        return

    df = df.copy()
    df.columns = df.columns.str.lower().str.strip()

    if "category" not in df.columns or "amount" not in df.columns:
        return

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)
    df["category"] = df["category"].astype(str).str.lower().str.strip()

    data = df[df["category"] != "income"].groupby("category")["amount"].sum()
    data = data[data > 0]

    if data.empty:
        return

    plt.figure(figsize=(5, 4))
    plt.pie(data.values, labels=data.index, autopct="%1.0f%%", radius=0.7)
    plt.title("Expense by Category")

    plt.savefig(get_path("category.png"), dpi=200, bbox_inches="tight")
    plt.close()


# ---------------- MONTHLY ----------------
def plot_monthly(df):
    if "date" not in df.columns:
        return

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    data = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()

    plt.figure(figsize=(5, 3))
    plt.plot(data.index.astype(str), data.values)
    plt.title("Monthly Trend")

    plt.tight_layout()
    plt.savefig(get_path("monthly.png"))
    plt.close()


# ---------------- DAILY ----------------
def plot_daily(df):
    if "date" not in df.columns:
        return

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    data = df.groupby(df["date"].dt.date)["amount"].sum()

    plt.figure(figsize=(5, 3))
    plt.plot(data.index, data.values)
    plt.title("Daily Trend")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(get_path("daily.png"))
    plt.close()


# ---------------- PAYMENT ----------------
def plot_payment(df):
    if "payment" not in df.columns:
        return

    df = df.copy()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    data = df.groupby("payment")["amount"].sum()

    if data.empty:
        return

    plt.figure(figsize=(4, 4))
    plt.bar(data.index, data.values)
    plt.title("Payment Methods")

    plt.tight_layout()
    plt.savefig(get_path("payment.png"))
    plt.close()


# ---------------- SUMMARY ----------------
def plot_summary(income, spend, savings):
    plt.figure(figsize=(4, 4))

    labels = ["Income", "Spend", "Savings"]
    values = [income, spend, savings]

    plt.bar(labels, values)
    plt.title("Summary")

    plt.tight_layout()
    plt.savefig(get_path("summary.png"))
    plt.close()