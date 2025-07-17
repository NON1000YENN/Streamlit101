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

#count each product sell each month
st.subheader("Product Sales Count by Region")
product_sales = df.groupby(['Product', 'Date']).size().reset_index(name='Count')

# Show a bar chart of product sales
st.subheader("Product Sales Bar Chart")
st.bar_chart(product_sales.set_index('Date')['Count'].groupby(product_sales['Product']).sum())

    