import streamlit as st
import pandas as pd


# page_config must me ON THE TOP OF FILE
st.set_page_config(
    page_title="Streamit 101",
    page_icon="🚀",  # ใช้ Unicode แทน :rocket:
    layout="wide"
)


st.markdown("<h1 style='text-align:center;'>CAD File Uploader Examplepage</h1>", unsafe_allow_html=True)

#Load Mock Data
df = pd.read_csv("mock_sales_data.csv")

#Show example of dataframe
st.subheader("Example of DataFrame")
st.dataframe(df.head(10), use_container_width=True)

# Convert 'Date' to datetime
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime('%Y-%m')  # Format: YYYY-MM

# Group by Month and Product, then sum Sales
monthly_sales = df.groupby(["Month", "Product"])["Sales"].sum().unstack().fillna(0)

# Plot
st.title("Monthly Product Sales")
st.bar_chart(monthly_sales)