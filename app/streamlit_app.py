import streamlit as st
import pandas as pd
import os

from src.visualization import (
    plot_category,
    plot_monthly,
    plot_daily,
    plot_payment,
    plot_summary,
    ensure_environment
)

st.set_page_config(
    page_title="Expense Tracker",
    layout="wide"
)

ensure_environment()


# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/expenses.csv")
    except:
        return pd.DataFrame({
            "date": pd.date_range("2025-01-01", periods=8),
            "category": ["income", "food", "rent", "shopping", "income", "bills", "transport", "food"],
            "amount": [60000, 2000, 10000, 3000, 80000, 1500, 1200, 2500],
            "payment": ["bank", "upi", "card", "upi", "bank", "upi", "cash", "upi"]
        })


df = load_data()

df.columns = df.columns.str.lower().str.strip()
df["category"] = df["category"].astype(str).str.lower().str.strip()
df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)


# ---------------- SIDEBAR (FIXED PROPER POSITION) ----------------
st.sidebar.title("🔍 Filters")

categories = ["All"] + sorted(df["category"].unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)


# ---------------- FILTER DATA ----------------
if selected_category != "All":
    df_view = df[df["category"] == selected_category]
else:
    df_view = df


# ---------------- CALCULATIONS ----------------
income = df[df["category"] == "income"]["amount"].sum()
spend = df[df["category"] != "income"]["amount"].sum()
savings = income - spend


# ---------------- TOP METRICS (PROPER ALIGNMENT) ----------------
st.title("💸 Personal Expense Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Spend", f"₹{spend:,.0f}")

with col2:
    st.metric("📈 Income", f"₹{income:,.0f}")

with col3:
    st.metric("💾 Savings", f"₹{savings:,.0f}")


st.divider()


# ---------------- TWO COLUMN LAYOUT (FIX SIZE ISSUE) ----------------
left, right = st.columns(2)


with left:
    st.subheader("📊 Category Breakdown")
    plot_category(df_view)
    if os.path.exists("outputs/charts/category.png"):
        st.image("outputs/charts/category.png", width=350)

    st.subheader("💳 Payment Methods")
    plot_payment(df_view)
    if os.path.exists("outputs/charts/payment.png"):
        st.image("outputs/charts/payment.png", width=350)


with right:
    st.subheader("📈 Monthly Trend")
    plot_monthly(df_view)
    if os.path.exists("outputs/charts/monthly.png"):
        st.image("outputs/charts/monthly.png", width=350)

    st.subheader("📉 Daily Trend")
    plot_daily(df_view)
    if os.path.exists("outputs/charts/daily.png"):
        st.image("outputs/charts/daily.png", width=350)


st.divider()

# ---------------- SUMMARY (CENTER SMALL CARD STYLE) ----------------
st.subheader("📌 Summary")

plot_summary(income, spend, savings)

if os.path.exists("outputs/charts/summary.png"):
    st.image("outputs/charts/summary.png", width=400)