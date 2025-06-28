#mysql_creator.py
import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": ""
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# ایجاد دیتابیس
cursor.execute("CREATE DATABASE IF NOT EXISTS base_bot")

# اتصال به دیتابیس
cursor.execute("USE base_bot")

# ایجاد جداول
cursor.execute("""
    CREATE TABLE IF NOT EXISTS allowed_users (
        user_id BIGINT PRIMARY KEY
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS all_users (
        user_id BIGINT PRIMARY KEY
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS message_counts (
        user_id BIGINT PRIMARY KEY,
        count INT DEFAULT 0
    )
""")

conn.commit()
cursor.close()
conn.close()