
import sqlite3
import matplotlib.pyplot as plt
import random
import timeit
import numpy as np


def main():
    global conn 
    global c

    # connect to small db 
    conn = sqlite3.connect('A3Small.db')
    c = conn.cursor()
    

    # creates tables
    schema = """
                        CREATE TABLE IF NOT EXISTS "Customers_Undefined" (
                        "customer_id" TEXT,
                        "customer_postal_code" INTEGER
                        );
                        CREATE TABLE IF NOT EXISTS "Sellers_Undefined" (
                        "seller_id" TEXT,
                        "seller_postal_code" INTEGER
                        );
                        CREATE TABLE IF NOT EXISTS "Orders_Undefined" (
                        "order_id" TEXT,
                        "customer_id" TEXT
                        );
                        CREATE TABLE IF NOT EXISTS "Order_items_Undefined" (
                        "order_id" TEXT,
                        "order_item_id" INTEGER,
                        "product_id" TEXT,
                        "seller_id" TEXT
                        );
                """
    c.executescript(schema)
            
    # Populate tables
    populateUndefined = """
                            INSERT INTO Customers_Undefined SELECT
                            customer_id,
                            customer_postal_code
                            FROM Customers;
                            
                            INSERT INTO Sellers_Undefined SELECT
                            seller_id,
                            seller_postal_code
                            FROM Sellers;
                            
                            INSERT INTO Orders_Undefined SELECT
                            order_id,
                            customer_id
                            FROM Orders;
                            
                            INSERT INTO Order_items_Undefined SELECT
                            order_id,
                            order_item_id,
                            product_id,
                            seller_id
                            FROM Order_items;
                            """
    c.executescript(populateUndefined)
    conn.commit()
    
    # Query uninformed 
    runtimeUninformedSmall = timeit.timeit('uninformed()', globals=globals(), number=50)
    print(f"Runtime of uniformed SMALL: {runtimeUninformedSmall} seconds")
    
    conn.close()
    conn = sqlite3.connect('A3Small.db')
    c = conn.cursor()
    
    # query uninformed
    runtimeSelfOptimizedSmall = timeit.timeit('selfOptimized()', globals=globals(), number=50)
    print(f"Runtime of Self-Optimized SMALL: {runtimeSelfOptimizedSmall} seconds")
    
    conn.close()
    conn = sqlite3.connect('A3Small.db')
    c = conn.cursor()
    
    # Create indexes for the user-optimized approach for the small database  
    c.execute("CREATE INDEX idx_customers_postal_code ON Customers(customer_postal_code);")
    c.execute("CREATE INDEX idx_orders_customer_id ON Orders(customer_id);")
    c.execute("CREATE INDEX idx_orders_order_id ON Orders(order_id);")
    c.execute("CREATE INDEX idx_order_items_order_id ON Order_items(order_id);")
    c.execute("CREATE INDEX idx_order_items_order_item_id ON Order_items(order_item_id);")
   
    runtimeUserOptimizedSmall = timeit.timeit('userOptimized()', globals=globals(), number=50)
    print(f"Runtime of User-Optimized SMALL: {runtimeUserOptimizedSmall} seconds")
    
    conn.commit()
    
    # # End and drop all the tables here for SMALL then close the database
    c.execute("DROP TABLE Customers_Undefined;")
    c.execute("DROP TABLE Sellers_Undefined;")
    c.execute("DROP TABLE Orders_Undefined;")
    c.execute(" DROP TABLE Order_items_Undefined;")
    c.execute("DROP INDEX idx_customers_postal_code ;")
    c.execute("DROP INDEX idx_orders_customer_id;")
    c.execute("DROP INDEX idx_orders_order_id;")
    c.execute("DROP INDEX idx_order_items_order_id ;")
    c.execute("DROP INDEX idx_order_items_order_item_id ;")
    
    
    conn.close()
    
    conn = sqlite3.connect('A3Medium.db')
    c = conn.cursor()

    # Populate the medium database with the undefined stuff to run
    c.executescript(schema)
    c.executescript(populateUndefined)
    conn.commit()
   
    # create view for medium database
    
     
    runtimeUninformedMedium= timeit.timeit('uninformed()', globals=globals(), number=50)
    print(f"Runtime of uniformed MEDIUM: {runtimeUninformedMedium} seconds")
    
    # Closing and re-opening for medium selfOptimized
    conn.close()
    conn = sqlite3.connect('A3Medium.db')
    c = conn.cursor()
    
    runtimeSelfOptimizedMedium = timeit.timeit('selfOptimized()', globals=globals(), number=50)
    print(f"Runtime of Self-Optimized MEDIUM: {runtimeSelfOptimizedMedium} seconds")
    
    # Closing and re-opening for medium userOPtimized
    conn.close()
    conn = sqlite3.connect('A3Medium.db')
    c = conn.cursor()
    
    c.execute("CREATE INDEX idx_customers_postal_code ON Customers(customer_postal_code);")
    c.execute("CREATE INDEX idx_orders_customer_id ON Orders(customer_id);")
    c.execute("CREATE INDEX idx_orders_order_id ON Orders(order_id);")
    c.execute("CREATE INDEX idx_order_items_order_id ON Order_items(order_id);")
    c.execute("CREATE INDEX idx_order_items_order_item_id ON Order_items(order_item_id);")

    runtimeUserOptimizedMedium = timeit.timeit('userOptimized()', globals=globals(), number=50)
    print(f"Runtime of User-Optimized MEDIUM: {runtimeUserOptimizedMedium} seconds")
    
    # Closing and reclosing for
    conn.commit()
    

    # End and drop all the tables here for SMALL then close the database
    c.execute("DROP TABLE Customers_Undefined;")
    c.execute("DROP TABLE Sellers_Undefined;")
    c.execute("DROP TABLE Orders_Undefined;")
    c.execute(" DROP TABLE Order_items_Undefined;")
    c.execute("DROP INDEX idx_customers_postal_code ;")
    c.execute("DROP INDEX idx_orders_customer_id;")
    c.execute("DROP INDEX idx_orders_order_id;")
    c.execute("DROP INDEX idx_order_items_order_id ;")
    c.execute("DROP INDEX idx_order_items_order_item_id ;")
    
    conn.close()
    conn = sqlite3.connect('A3Large.db')
    c = conn.cursor()
    
    # Populate the medium database with the undefined stuff to run
    c.executescript(schema)
    c.executescript(populateUndefined)
    conn.commit()
    
    # create view for medium database
   
    
    # Large database uninformed
    runtimeUninformedLarge= timeit.timeit('uninformed()', globals=globals(), number=50)
    print(f"Runtime of uniformed Large: {runtimeUninformedLarge} seconds")
    
    # Closing and-reopening for large self-optimized
    conn.close()
    conn = sqlite3.connect('A3Large.db')
    c = conn.cursor()
    
    runtimeSelfOptimizedLarge = timeit.timeit('selfOptimized()', globals=globals(), number=50)
    print(f"Runtime of Self-Optimized Large: {runtimeSelfOptimizedLarge} seconds")
    
    
    # Closing and re-opening for medium userOPtimized LARGE
    conn.close()
    conn = sqlite3.connect('A3Large.db')
    c = conn.cursor()
    
    # Indexes for LARGE
    c.execute("CREATE INDEX idx_customers_postal_code ON Customers(customer_postal_code);")
    c.execute("CREATE INDEX idx_orders_customer_id ON Orders(customer_id);")
    c.execute("CREATE INDEX idx_orders_order_id ON Orders(order_id);")
    c.execute("CREATE INDEX idx_order_items_order_id ON Order_items(order_id);")
    c.execute("CREATE INDEX idx_order_items_order_item_id ON Order_items(order_item_id);")
    
    
    runtimeUserOptimizedLarge = timeit.timeit('userOptimized()', globals=globals(), number=50)
    print(f"Runtime of User-Optimized LArge: {runtimeUserOptimizedLarge} seconds")
    
    conn.commit()
    

    # # End and drop all the tables here for SMALL then close the database
    c.execute("DROP TABLE Customers_Undefined;")
    c.execute("DROP TABLE Sellers_Undefined;")
    c.execute("DROP TABLE Orders_Undefined;")
    c.execute(" DROP TABLE Order_items_Undefined;")
    c.execute("DROP INDEX idx_customers_postal_code ;")
    c.execute("DROP INDEX idx_orders_customer_id;")
    c.execute("DROP INDEX idx_orders_order_id;")
    c.execute("DROP INDEX idx_order_items_order_id ;")
    c.execute("DROP INDEX idx_order_items_order_item_id ;")
    
     # Plotting
    databaseSizes = ['smallDB', 'mediumDB', 'LargeDB']
    runtimeUninformed = [runtimeUninformedSmall, runtimeUninformedMedium, runtimeUninformedLarge]
    runtimeSelfOptimized = [runtimeSelfOptimizedSmall, runtimeSelfOptimizedMedium, runtimeSelfOptimizedLarge]
    runtimeUserOptimized = [runtimeUserOptimizedSmall, runtimeUserOptimizedMedium, runtimeUserOptimizedLarge]

    # bar width
    width = 0.2

    # create an array of x-axis positions for each group of bars
    x = np.arange(len(databaseSizes))

    # create side-by-side bars
    plt.bar(x - width, runtimeUninformed, width, label='Uninformed')
    plt.bar(x, runtimeSelfOptimized, width, label='Self-Optimized')
    plt.bar(x + width, runtimeUserOptimized, width, label='User-Optimized')

    # set x-ticks and labels
    plt.xticks(x, databaseSizes)

    # set axis labels and title
    plt.xlabel('Database sizes')
    plt.ylabel('Runtime (ms)')
    plt.title('Query 3 (average runtime in seconds)')

    # add legend
    plt.legend()

    # show plot
    plt.show()



#Then under here repopulate the the database except without the primary/foreign keys with new table so in the samll table instead of 4 there should be 8 now 

############## --> Scenarios <-- ##############

# Uninformed
def uninformed():
    i = 0
# Undefining the primary & foreign keys of all tables
    c.execute('''PRAGMA foreign_keys = OFF;''')
    
    
    
    # Disabling the creating of SQLite's auto indexing
    c.execute('''PRAGMA automatic_index = FALSE;''')
    
    
    # !! EXECUTE THE UNDEFINED SCRIPTS HERE LATER THEN USE THE UNDEFINED ONES
    
        # Grab all the postal code from 10,000 customers
    c.execute("SELECT customer_postal_code FROM Customers_Undefined")
    
    postal_codes = c.fetchall()
    # print(postal_codes)
    random_postal_code = random.choice(postal_codes)[0] #0 cuz since we are only executing to get postal codes it'll be in the first always
    # print("Random postal code for uninformed:")
    # print(random_postal_code)
    # print("")
    c.execute(
        """
  SELECT COUNT(*)
FROM Orders_Undefined
WHERE customer_id IN (
    SELECT customer_id
    FROM Customers_Undefined
    WHERE customer_postal_code = ?
)
AND order_id IN (
    SELECT order_id
    FROM Order_items_Undefined
    GROUP BY order_id
    HAVING COUNT(*) > (
        SELECT AVG(item_count)
        FROM (
            SELECT COUNT(*) as item_count
            FROM Order_items_Undefined
            GROUP BY order_id
        ) as item_counts
    )
)
    """, (random_postal_code,)
    )
    i+=1
    
    # result = c.fetchone()
    # print(result)
        





# SELF OPTIMIZED STARTS HERE #

# ----------------------------------
# conn2 is what we shall be using for self optimized to not get confused with the uniformed one
# conn2 = sqlite3.connect('A3Small.db')
# c2 = conn2.cursor()
# -----------------------------------


# Self-optimized

def selfOptimized():
    i = 0
    
    # Undefining the primary & foreign keys of all tables
    c.execute('''PRAGMA foreign_keys = ON;''')
    # Disabling the creating of SQLite's auto indexing
    c.execute('''PRAGMA automatic_index = TRUE;''')
    
    c.execute("SELECT customer_postal_code FROM Customers")
    
    postal_codes = c.fetchall()
    # print(postal_codes)
    random_postal_code = random.choice(postal_codes)[0] #0 cuz since we are only executing to get postal codes it'll be in the first always
    # print("Random postal code for Self-Optimized:")
    # print(random_postal_code)

    c.execute(
        """
       SELECT COUNT(*)
FROM Orders
WHERE customer_id IN (
    SELECT customer_id
    FROM Customers
    WHERE customer_postal_code = ?
)
AND order_id IN (
    SELECT order_id
    FROM Order_items
    GROUP BY order_id
    HAVING COUNT(*) > (
        SELECT AVG(item_count)
        FROM (
            SELECT COUNT(*) as item_count
            FROM Order_items
            GROUP BY order_id
        ) as item_counts
    )
)
    """, (random_postal_code,)
    )
    i += 1
    # result = c2.fetchone()
    # print(result)
    



# User-optimized
def userOptimized():
    i = 0
    # Undefining the primary & foreign keys of all tables
    c.execute('''PRAGMA foreign_keys = ON;''')
        # Disabling the creating of SQLite's auto indexing
    c.execute('''PRAGMA automatic_index = FALSE;''')
    
    
    c.execute("SELECT customer_postal_code FROM Customers")
        
    postal_codes = c.fetchall()
        # print(postal_codes)
    random_postal_code = random.choice(postal_codes)[0] #0 cuz since we are only executing to get postal codes it'll be in the first always
    # print("Random postal code for Self-Optimized:")
    # print(random_postal_code)

    c.execute(
        """
               SELECT COUNT(*)
FROM Orders
WHERE customer_id IN (
    SELECT customer_id
    FROM Customers
    WHERE customer_postal_code = ?
)
AND order_id IN (
    SELECT order_id
    FROM Order_items
    GROUP BY order_id
    HAVING COUNT(*) > (
        SELECT AVG(item_count)
        FROM (
            SELECT COUNT(*) as item_count
            FROM Order_items
            GROUP BY order_id
        ) as item_counts
    )
)
    """, (random_postal_code,)
    )
        # result = c2.fetchone()
        # print(result)
    
    i += 1
        
main()

