import streamlit as st
import pandas as pd

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ModuleNotFoundError:
    plt = None
    MATPLOTLIB_AVAILABLE = False

from database.db import get_expenses, get_budgets, get_emis
from utils.helpers import convert_expenses_to_df, convert_budgets_to_df, convert_emis_to_df
from utils.auth import is_logged_in
from utils.alerts import generate_spending_alerts

st.title("📈 Reports Dashboard")

if not is_logged_in():
    st.warning("Please login first.")
    st.stop()

user = st.session_state.user
user_id = user[0]
salary = user[3]
savings_goal = user[4]

expenses = get_expenses(user_id)
budgets = get_budgets(user_id)
emis = get_emis(user_id)

df_exp = convert_expenses_to_df(expenses)
df_budget = convert_budgets_to_df(budgets)
df_emi = convert_emis_to_df(emis)

# Total EMI calculation
total_emi = df_emi["Monthly EMI"].sum() if not df_emi.empty else 0

if df_exp.empty:
    st.warning("No expense records found.")
    st.stop()

total_spent = df_exp["Amount"].sum()
total_outflow = total_spent + total_emi
remaining_balance = salary - total_outflow

st.subheader("📌 Monthly Summary")
st.metric("Salary", f"₹{salary:.2f}")
st.metric("Total Expenses", f"₹{total_spent:.2f}")
st.metric("Total EMI Payments", f"₹{total_emi:.2f}")
st.metric("Remaining Balance", f"₹{remaining_balance:.2f}")

# Savings Alert
if remaining_balance < savings_goal:
    st.error("⚠️ Warning: You may not reach your savings goal this month!")

# AI Alerts
st.subheader("🚨 Smart Spending Alerts")
alerts = generate_spending_alerts(df_exp, salary)

if alerts:
    for alert in alerts:
        st.warning(alert)
else:
    st.success("✅ Great! Your spending is under control.")

# Category wise spending
st.subheader("📌 Category-wise Spending")
category_spend = df_exp.groupby("Category")["Amount"].sum()

if MATPLOTLIB_AVAILABLE:
    fig1, ax1 = plt.subplots()
    category_spend.plot(kind="bar", ax=ax1)
    st.pyplot(fig1)
else:
    st.warning("matplotlib is unavailable; chart display is disabled. Install matplotlib in requirements.txt to enable it.")

# Fixed vs Variable analysis
st.subheader("📌 Fixed vs Variable Expense Analysis")
type_spend = df_exp.groupby("Type")["Amount"].sum()

if MATPLOTLIB_AVAILABLE:
    fig2, ax2 = plt.subplots()
    type_spend.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    st.pyplot(fig2)

# Monthly Trend Graph
st.subheader("📆 Monthly Trend Report")

df_exp["Date"] = pd.to_datetime(df_exp["Date"])
df_exp["Month"] = df_exp["Date"].dt.to_period("M").astype(str)

monthly_trend = df_exp.groupby("Month")["Amount"].sum()

if MATPLOTLIB_AVAILABLE:
    fig3, ax3 = plt.subplots()
    monthly_trend.plot(kind="line", marker="o", ax=ax3)
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Spending (₹)")
    st.pyplot(fig3)
else:
    st.info("Monthly trend chart unavailable because matplotlib is not installed.")

# Download Report
st.subheader("📥 Download Expense Report")
csv = df_exp.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "expense_report.csv", "text/csv")
