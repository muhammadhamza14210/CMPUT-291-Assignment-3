import sqlite3
import csv
import random

# Define the schema
schema = """
CREATE TABLE "Customers" (
"customer_id" TEXT,
"customer_postal_code" INTEGER,
PRIMARY KEY("customer_id")
);

CREATE TABLE "Sellers" (
"seller_id" TEXT,
"seller_postal_code" INTEGER,
PRIMARY KEY("seller_id")
);

CREATE TABLE "Orders" (
"order_id" TEXT,
"customer_id" TEXT,
PRIMARY KEY("order_id"),
FOREIGN KEY("customer_id") REFERENCES "Customers"("customer_id")
);

CREATE TABLE "Order_items" (
"order_id" TEXT,
"order_item_id" INTEGER,
"product_id" TEXT,
"seller_id" TEXT,
PRIMARY KEY("order_id","order_item_id","product_id","seller_id"),
FOREIGN KEY("seller_id") REFERENCES "Sellers"("seller_id"),
FOREIGN KEY("order_id") REFERENCES "Orders"("order_id")
);
"""

# Connect to the database
conn = sqlite3.connect('Small.db')

# Create the tables in the database
c = conn.cursor()
c.executescript(schema)
c.execute('''PRAGMA foreign_keys = ON;''')
# Load a random sample of data into the Customers table
with open('archive/olist_customers_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    num_rows = 10000 #Change to how many you need for CUSTOMERS the case of small, medium, large
    sample_rows = random.sample(list(reader), num_rows)
    line = 0
    for row in sample_rows:
        # print(row[0], row[2])
        c.execute("INSERT INTO Customers VALUES (?, ?);", (row[0], row[2]))
        # line +=1
# print(line)


# Load a random sample of data into the Sellers table
with open('archive/olist_sellers_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    num_rows = 500 #Change to how many you need SELLERS for the case of small, medium, large
    sample_rows = random.sample(list(reader), num_rows)
    for row in sample_rows:
        c.execute("INSERT INTO Sellers VALUES (?, ?)", (row[0], row[1]))

with open('archive/olist_orders_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    num_rows = 99441 #THIS VALUE STAYS THE SAME ALWAYS as per the csv file
    sample_rows = random.sample(list(reader), num_rows)
    for row in sample_rows:
        try:
            c.execute("INSERT INTO Orders VALUES (?, (SELECT Customers.customer_id FROM Orders, Customers WHERE Customers.customer_id = ?))", (row[0], row[1]))
        except sqlite3.IntegrityError:
            # Ignore duplicate primary key errors
            pass

# From orders dataset the above query will run and some will have NULL values so this below should take care of that
# Would then result in everything in the customers table have an order in the orders table
c.execute('''
          
        DELETE FROM ORDERS
        WHERE ORDERS.customer_id IS NULL
          '''
          )


# Same thing for order items
with open('archive/olist_order_items_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    num_rows = 112650 #THIS VALUE STAYS THE SAME ALWAYS as per the csv file
    sample_rows = random.sample(list(reader), num_rows)
    for row in sample_rows:
        try:
            c.execute("INSERT INTO Order_items VALUES ((SELECT Orders.order_id FROM Orders, Order_items WHERE Orders.order_id = ?), ? ,?, (SELECT Sellers.seller_id FROM Sellers, Order_items WHERE Sellers.seller_id = ?))", (row[0], row[1], row[2], row[3]))
        except sqlite3.IntegrityError:
            # Ignore duplicate primary key errors
            pass
c.execute('''
          
        DELETE FROM Order_items
        WHERE order_id IS NULL OR seller_id IS NULL
          '''
          )
conn.commit()