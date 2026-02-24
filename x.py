import os
import pandas as pd
import mysql.connector

# Setup output folder
output_dir = r"C:\Users\A1\OneDrive\Desktop\ecommerce_bi"
os.makedirs(output_dir, exist_ok=True)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_bi"
)

# 1️⃣ All customers
df_all = pd.read_sql("SELECT * FROM `customers-100`", conn)
df_all.to_csv(os.path.join(output_dir, "customers_all.csv"), index=False)

# 2️⃣ US customers
df_us = pd.read_sql(
    "SELECT * FROM `customers-100` WHERE Country LIKE '%United States%'",
    conn
)
df_us.to_csv(os.path.join(output_dir, "customers_us.csv"), index=False)

# 3️⃣ Latest subscriptions (top 10)
df_latest = pd.read_sql(
    "SELECT * FROM `customers-100` ORDER BY `Subscription Date` DESC LIMIT 10",
    conn
)
df_latest.to_csv(os.path.join(output_dir, "customers_latest.csv"), index=False)

print("All CSV files saved in:", output_dir)




