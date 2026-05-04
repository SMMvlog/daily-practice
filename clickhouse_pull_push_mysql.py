import pandas as pd
import mysql.connector
import clickhouse_connect

# -------------------------------
# 1️⃣ MySQL connection details
# -------------------------------
mysql_config = {
    'host': 'localhost',        # MySQL host
    'user': 'root',             # MySQL username
    'password': 'root',
    'database': 'proj1',      # MySQL database name
    'port': 3306
}

# -------------------------------
# 2️⃣ ClickHouse connection details
# -------------------------------
clickhouse_config = {
    'host': '127.0.0.1',
    'port': 8123,
    'username': 'default',
    'password': 'yourpassword123',
    'database': 'default'
}



# -------------------------------
# 3️⃣ Fetch data from MySQL
# -------------------------------
mysql_conn = mysql.connector.connect(**mysql_config)
query = "SELECT emp_id, emp_name,emp_salary,joining_date FROM employee_master;"  # change table & columns as needed
df = pd.read_sql(query, mysql_conn)
print("sadasffffff-----",df)
mysql_conn.close()

print(f"✅ Pulled {len(df)} rows from MySQL")

# -------------------------------
# 4️⃣ Connect to ClickHouse
# -------------------------------
ch_client = clickhouse_connect.get_client(**clickhouse_config)

# -------------------------------
# 5️⃣ Create ClickHouse table (if not exists)
# -------------------------------
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    emp_id Int32,
    emp_name String,
    emp_salary Decimal(10,2),
    joining_date Date
) ENGINE = MergeTree()
ORDER BY emp_id
"""
ch_client.command(create_table_query)

# -------------------------------
# 6️⃣ Insert data into ClickHouse
# -------------------------------
ch_client.insert_df('users', df)
print(f"✅ Inserted {len(df)} rows into ClickHouse")

# -------------------------------
# 7️⃣ Verify data count
# -------------------------------
result = ch_client.query("SELECT count() FROM users")
print(f"📊 Total rows in ClickHouse table: {result.result_rows[0][0]}")
