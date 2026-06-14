import streamlit as st
import pandas as pd

st.title("Neural Retail Analytics Dashboard")

df = pd.read_csv("clean_data.csv")

df["Sales"] = df["Quantity"] * df["UnitPrice"]

st.dataframe(df.head())

st.metric("Total Sales", round(df["Sales"].sum(), 2))
st.metric("Total Customers", df["CustomerID"].nunique())

st.bar_chart(df.groupby("Country")["Sales"].sum())