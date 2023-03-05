import sqlite3
import matplotlib.pyplot as plt

import timeit
import numpy as np

def main():
    global conn 
    conn = sqlite3.connect('A3Small.db')
    global c
    c = conn.cursor()
    schema = """
                        
                        CREATE TABLE "Customers_Undefined" (
                        "customer_id" TEXT,
                        "customer_postal_code" INTEGER
                        
                        );

                        CREATE TABLE "Sellers_Undefined" (
                        "seller_id" TEXT,
                        "seller_postal_code" INTEGER
                        
                        );

                        CREATE TABLE "Orders_Undefined" (
                        "order_id" TEXT,
                        "customer_id" TEXT
                        
                        );

                        CREATE TABLE "Order_items_Undefined" (
                        "order_id" TEXT,
                        "order_item_id" INTEGER,
                        "product_id" TEXT,
                        "seller_id" TEXT
                        
                        
                        );
                """
    c.executescript(schema)
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
            # Then go on
    c.executescript(populateUndefined)
    conn.commit()
    
    # -------------------------Small database---------------------------------#
    # uninformed()
    runtimeUninformedSmall = timeit.timeit('uninformed()', globals=globals(), number=50)
    print(f"Runtime of uniformed SMALL: {runtimeUninformedSmall} seconds")
    
    

    
    # User optimized close and re-open
    
    # Self-Optimized
    # OPening/Reclosing
    conn.close()
    conn = sqlite3.connect('A3Small.db')
    c = conn.cursor()
    
    # selfOptimized()
    runtimeSelfOptimizedSmall = timeit.timeit('selfOptimized()', globals=globals(), number=50)
    print(f"Runtime of Self-Optimized SMALL: {runtimeSelfOptimizedSmall} seconds")
    
    
    conn.close()
    conn = sqlite3.connect('A3Small.db')
    c = conn.cursor()
        
    c.execute("CREATE INDEX idx_customers_customer_id ON Customers (customer_id);")
    c.execute("CREATE INDEX idx_sellers_seller_postal_code ON Sellers (seller_postal_code);")
    c.execute("CREATE INDEX idx_orders_customer_id ON Orders (customer_id);")
    c.execute("CREATE INDEX idx_orders_order_id ON Orders (order_id);")
    c.execute("CREATE INDEX idx_order_items_order_id ON Order_items (order_id);")
    c.execute(" CREATE INDEX idx_order_items_seller_id ON Order_items (seller_id);")
    

    
    runtimeUserOptimizedSmall = timeit.timeit('userOptimized()', globals=globals(), number=50)
    print(f"Runtime of User-Optimized SMALL: {runtimeUserOptimizedSmall} seconds")
    
    # Drop tables/Indexes for later
    c.execute("DROP TABLE Customers_Undefined;")
    c.execute("DROP TABLE Sellers_Undefined;")
    c.execute("DROP TABLE Orders_Undefined;")
    c.execute(" DROP TABLE Order_items_Undefined;")
    
    c.execute("DROP INDEX idx_customers_customer_id ;")
    c.execute("DROP INDEX idx_sellers_seller_postal_code;")
    c.execute("DROP INDEX idx_orders_customer_id;")
    c.execute("DROP INDEX idx_orders_order_id;")
    c.execute("DROP INDEX idx_order_items_order_id;")
    c.execute("DROP INDEX idx_order_items_seller_id;")
    
    
   
    # -------------------------Medium Database starts here----------------------------------#
    conn.commit()
    conn.close()
    conn = sqlite3.connect('A3Medium.db')
    c = conn.cursor()
    # Populate the medium database with the undefined stuff to run
    c.executescript(schema)
    c.executescript(populateUndefined)
    conn.commit()
    
     # uninformed()
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
    
    c.execute("CREATE INDEX idx_customers_customer_id ON Customers (customer_id);")
    c.execute("CREATE INDEX idx_sellers_seller_postal_code ON Sellers (seller_postal_code);")
    c.execute("CREATE INDEX idx_orders_customer_id ON Orders (customer_id);")
    c.execute("CREATE INDEX idx_orders_order_id ON Orders (order_id);")
    c.execute("CREATE INDEX idx_order_items_order_id ON Order_items (order_id);")
    c.execute(" CREATE INDEX idx_order_items_seller_id ON Order_items (seller_id);")
    runtimeUserOptimizedMedium = timeit.timeit('userOptimized()', globals=globals(), number=50)
    print(f"Runtime of User-Optimized Medium: {runtimeUserOptimizedMedium} seconds")
    
     # Drop tables/Indexes for later
    c.execute("DROP TABLE Customers_Undefined;")
    c.execute("DROP TABLE Sellers_Undefined;")
    c.execute("DROP TABLE Orders_Undefined;")
    c.execute(" DROP TABLE Order_items_Undefined;")
    
    c.execute("DROP INDEX idx_customers_customer_id ;")
    c.execute("DROP INDEX idx_sellers_seller_postal_code;")
    c.execute("DROP INDEX idx_orders_customer_id;")
    c.execute("DROP INDEX idx_orders_order_id;")
    c.execute("DROP INDEX idx_order_items_order_id;")
    c.execute("DROP INDEX idx_order_items_seller_id;")
    
    
    # ------------------------------Large Database Starts Here ---------------------------------#
    conn.commit()
    conn.close()
    conn = sqlite3.connect('A3Large.db')
    c = conn.cursor()
    # Populate the Large database with the undefined stuff to run
    c.executescript(schema)
    c.executescript(populateUndefined)
    conn.commit()
    
     # uninformed()
    runtimeUninformedLarge= timeit.timeit('uninformed()', globals=globals(), number=50)
    print(f"Runtime of uniformed Large: {runtimeUninformedLarge} seconds")
    
    # Closing and re-opening for Large selfOptimized
    conn.close()
    conn = sqlite3.connect('A3Large.db')
    c = conn.cursor()
    
    runtimeSelfOptimizedLarge = timeit.timeit('selfOptimized()', globals=globals(), number=50)
    print(f"Runtime of Self-Optimized Large: {runtimeSelfOptimizedLarge} seconds")
    
    # Closing and re-opening for Large userOPtimized
    conn.close()
    conn = sqlite3.connect('A3Large.db')
    c = conn.cursor()
    
    c.execute("CREATE INDEX idx_customers_customer_id ON Customers (customer_id);")
    c.execute("CREATE INDEX idx_sellers_seller_postal_code ON Sellers (seller_postal_code);")
    c.execute("CREATE INDEX idx_orders_customer_id ON Orders (customer_id);")
    c.execute("CREATE INDEX idx_orders_order_id ON Orders (order_id);")
    c.execute("CREATE INDEX idx_order_items_order_id ON Order_items (order_id);")
    c.execute(" CREATE INDEX idx_order_items_seller_id ON Order_items (seller_id);")
    
    runtimeUserOptimizedLarge = timeit.timeit('userOptimized()', globals=globals(), number=50)
    print(f"Runtime of User-Optimized Large: {runtimeUserOptimizedLarge} seconds")
    
     # Drop tables/Indexes for later
    c.execute("DROP TABLE Customers_Undefined;")
    c.execute("DROP TABLE Sellers_Undefined;")
    c.execute("DROP TABLE Orders_Undefined;")
    c.execute(" DROP TABLE Order_items_Undefined;")
    
    c.execute("DROP INDEX idx_customers_customer_id ;")
    c.execute("DROP INDEX idx_sellers_seller_postal_code;")
    c.execute("DROP INDEX idx_orders_customer_id;")
    c.execute("DROP INDEX idx_orders_order_id;")
    c.execute("DROP INDEX idx_order_items_order_id;")
    c.execute("DROP INDEX idx_order_items_seller_id;")
    
     # Plotting
    databaseSizes = ['smallDB', 'mediumDB', 'LargeDB']
    runtimeUninformed = [runtimeUninformedSmall*20, runtimeUninformedMedium*20, runtimeUninformedLarge*20]
    runtimeSelfOptimized = [runtimeSelfOptimizedSmall*20, runtimeSelfOptimizedMedium*20, runtimeSelfOptimizedLarge*20]
    runtimeUserOptimized = [runtimeUserOptimizedSmall*20, runtimeUserOptimizedMedium*20, runtimeUserOptimizedLarge*20]

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
    plt.title('Query 4 (average runtime in milliseconds)')

    # add legend
    plt.legend()

    # show plot
    plt.show()

def uninformed():
    # Undefine our primary / foreign keys 
    c.execute('''PRAGMA foreign_keys = OFF;''')
    
    
    
    # Disabling the creating of SQLite's auto indexing
    c.execute('''PRAGMA automatic_index = FALSE;''')
    
    # I shall be splitting by query into 3 parts
    #1) Grab a random customer with more than 1 order
    #2) For that random customer with more than 1 order show all their orders and the seller_id its linked to then grab that
    #3) Using that seller_id find all the postal codes and add them to a set which will take care of duplicity for us and all we need to do is count the set from then
    # Grab all the customers with more than 1 order and choose a random one
    
    
    # 1
    c.execute("""
              
            SELECT COUNT(DISTINCT Sellers_Undefined.seller_postal_code)
FROM Customers_Undefined, Sellers_Undefined
WHERE Customers_Undefined.customer_id IN (
    SELECT Orders_Undefined.customer_id
    FROM Orders_Undefined
    WHERE Orders_Undefined.order_id IN (
        SELECT Order_items_Undefined.order_id
        FROM Order_items_Undefined
        WHERE Order_items_Undefined.seller_id IN (
            SELECT Sellers_Undefined.seller_id
            FROM Sellers_Undefined
        )
    )
    GROUP BY Orders_Undefined.customer_id
    HAVING COUNT(*) > 1
)
ORDER BY RANDOM()
LIMIT 1;
            """)
    
                
    allCustomers = c.fetchall()
    # print(allCustomers)

    
def selfOptimized():
        # Undefine our primary / foreign keys 
    c.execute('''PRAGMA foreign_keys = ON;''')
    
    
    
    # Disabling the creating of SQLite's auto indexing
    c.execute('''PRAGMA automatic_index = TRUE;''')
    
    c.execute("""
            SELECT COUNT(DISTINCT Sellers.seller_postal_code)
FROM Customers, Sellers
WHERE Customers.customer_id IN (
    SELECT Orders.customer_id
    FROM Orders
    WHERE Orders.order_id IN (
        SELECT Order_items.order_id
        FROM Order_items
        WHERE Order_items.seller_id IN (
            SELECT Sellers.seller_id
            FROM Sellers
        )
    )
    GROUP BY Orders.customer_id
    HAVING COUNT(*) > 1
)
ORDER BY RANDOM()
LIMIT 1;
            
            """)
    
                
    allCustomers = c.fetchall()
    # print(allCustomers)

def userOptimized():
        # Undefine our primary / foreign keys 
    c.execute('''PRAGMA foreign_keys = ON;''')
    
    
    
    # Disabling the creating of SQLite's auto indexing
    c.execute('''PRAGMA automatic_index = TRUE;''')
    

    
    c.execute("""
            
        SELECT COUNT(DISTINCT Sellers.seller_postal_code)
        FROM Customers, Sellers
        WHERE Customers.customer_id IN (
            SELECT Orders.customer_id
            FROM Orders
            WHERE Orders.order_id IN (
                SELECT Order_items.order_id
                FROM Order_items
                WHERE Order_items.seller_id IN (
                    SELECT Sellers.seller_id
                    FROM Sellers
                )
            )
            GROUP BY Orders.customer_id
            HAVING COUNT(*) > 1
        )
        ORDER BY RANDOM()
        LIMIT 1;
                    
            """)
        
                    
    allCustomers = c.fetchall()
    # print(allCustomers)

main()
