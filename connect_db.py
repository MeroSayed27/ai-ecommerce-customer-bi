import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",       # your MySQL password
    database="ecommerce_bi"
)

# Read the table into a pandas DataFrame
df = pd.read_sql("SELECT * FROM `customers-100`", conn)

# Export to CSV on your Desktop
df.to_csv(r"C:\Users\A1\OneDrive\Desktop\ecommerce_bi\customers_all.csv", index=False)

conn.close()
print("Export complete ✅")