import streamlit as st
import pandas as pd

st.title("E-commerce Customer BI Dashboard")

# Load CSV
df = pd.read_csv(r"C:\Users\A1\OneDrive\Desktop\ecommerce_bi\customers_all.csv")

st.write("Total customers:", len(df))
st.dataframe(df.head(10))

# Filter by country
country = st.selectbox("Select Country", df['Country'].unique())
st.dataframe(df[df['Country'] == country])

