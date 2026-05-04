import pandas as pd
import clickhouse_connect
import mysql.connector

# -------------------------------
# 1️⃣ ClickHouse connection
# -------------------------------
clickhouse_config = {
    'host': '127.0.0.1',
    'port': 8123,
    'username': 'default',
    'password': 'yourpassword123',
    'database': 'default'
}

ch_client = clickhouse_connect.get_client(**clickhouse_config)

# -------------------------------
# 2️⃣ Create ClickHouse 'city' table
# -------------------------------
create_table_query = """
CREATE TABLE IF NOT EXISTS city (
    city_id Int32,
    city_name String,
    city_state String
) ENGINE = MergeTree()
ORDER BY city_id
"""
ch_client.command(create_table_query)

# -------------------------------
# 3️⃣ Insert 10 sample records into ClickHouse
# -------------------------------
data = [
    (1, 'Mumbai', 'Maharashtra'),
    (2, 'Delhi', 'Delhi'),
    (3, 'Bengaluru', 'Karnataka'),
    (4, 'Chennai', 'Tamil Nadu'),
    (5, 'Kolkata', 'West Bengal'),
    (6, 'Hyderabad', 'Telangana'),
    (7, 'Pune', 'Maharashtra'),
    (8, 'Ahmedabad', 'Gujarat'),
    (9, 'Jaipur', 'Rajasthan'),
    (10, 'Lucknow', 'Uttar Pradesh')
]

df = pd.DataFrame(data, columns=['city_id', 'city_name', 'city_state'])

ch_client.insert_df('city', df)
print("✅ Inserted 10 records into ClickHouse 'city' table")

# -------------------------------
# 4️⃣ MySQL connection
# -------------------------------
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'proj1',
    'port': 3306
}

mysql_conn = mysql.connector.connect(**mysql_config)
cursor = mysql_conn.cursor()

# -------------------------------
# 5️⃣ Create MySQL 'city' table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS city (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(100),
    city_state VARCHAR(100)
)
""")

# -------------------------------
# 6️⃣ Push data from ClickHouse to MySQL
# -------------------------------
# Fetch data from ClickHouse
ch_data = ch_client.query("SELECT city_id, city_name, city_state FROM city").result_rows

# Insert into MySQL
insert_query = "INSERT INTO city (city_id, city_name, city_state) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, ch_data)
mysql_conn.commit()

print(f"✅ Pushed {cursor.rowcount} records from ClickHouse to MySQL")

cursor.close()
mysql_conn.close()
