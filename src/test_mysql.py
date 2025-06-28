# test_mysql.py
import config
import mysql.connector

def test_connection():
    conn = mysql.connector.connect(**config.MYSQL_CONFIG)
    if conn.is_connected():
        print("اتصال موفقیت‌آمیز به MySQL!")
        conn.close()
    else:
        print("اتصال ناموفق!")

test_connection()