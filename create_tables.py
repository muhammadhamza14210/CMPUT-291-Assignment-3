def define_tables(connection,cursor):
    
    cursor.execute('''PRAGMA foreign_keys = ON;''')
    customers_query=   '''
                        CREATE TABLE Customers (
                                    customer_id TEXT,
                                    customer_postal_code INTEGER,
                                    PRIMARY KEY (customer_id)
                                    );
                    '''

    sellers_query=  '''
                        CREATE TABLE Sellers (
                                    seller_id TEXT,
                                    seller_postal_code INTEGER,
                                    PRIMARY KEY (seller_id)
                                    );
                    '''
                    
    order_query=    '''
                        CREATE TABLE Orders(
                                    order_id TEXT,
                                    customer_id TEXT,
                                    PRIMARY KEY (order_id),
                                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)   
                        )
                    
                    '''

    orders_items_query= '''
                    CREATE TABLE Order_items (
                                order_id TEXT,
                                order_item_id INTEGER,
                                product_id TEXT,
                                seller_id TEXT,
                                PRIMARY KEY (order_id, order_item_id, product_id, seller_id),
                                FOREIGN KEY(seller_id) REFERENCES Sellers(seller_id),
                                FOREIGN KEY(order_id) REFERENCES Orders(order_id)
                                );
                '''

    cursor.execute(customers_query)
    cursor.execute(sellers_query)
    cursor.execute(order_query)
    cursor.execute(orders_items_query)
    
    print("CREATED ALL TABLES")
