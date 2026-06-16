import streamlit as st
import pandas as pd

st.title("Neural Retail Analytics Dashboard")

df = pd.read_csv("clean_data.csv")

df["Sales"] = df["Quantity"] * df["UnitPrice"]

st.subheader("Data Preview")
st.dataframe(df.head())

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", round(df["Sales"].sum(), 2))

with col2:
    st.metric("Total Customers", df["CustomerID"].nunique())

st.subheader("Sales by Country")
country_sales = df.groupby("Country")["Sales"].sum()
st.bar_chart(country_sales)