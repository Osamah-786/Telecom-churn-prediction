import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="osamah@786",
    database="telecom_churn"
)

cursor = conn.cursor()

print("Connected to MySQL")