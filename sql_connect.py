import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost", user="root", passwd="my-secret-pw"
)

# Create a cursor
cursor = connection.cursor()

# # Execute a query(create a database)
# cursor.execute("CREATE DATABASE mydatabase")

# select the database
cursor.execute("USE mydatabase")

# Execute a query(create a table)
# cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# # Execute a query(insert data)
# cursor.execute(
#     "INSERT INTO customers (name, address) VALUES (%s, %s)", ("John", "Highway 21")
# )

# connection.commit()

# Execute a query(print all data)
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()
for x in result:
    print(x)

# close the connection
connection.close()
