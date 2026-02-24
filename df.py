import os
import pandas as pd
import mysql.connector

# Create folder if it doesn't exist
output_dir = r"C:\Users\A1\OneDrive\Desktop\ecommerce_bi"
os.makedirs(output_dir, exist_ok=True)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_bi"
)

# Read table into pandas
df = pd.read_sql("SELECT * FROM `customers-100`", conn)

# Save CSV
output_path = os.path.join(output_dir, "customers_all.csv")
df.to_csv(output_path, index=False)

print(f"CSV saved at {output_path}")