import sqlite3

connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return

def define_tables():
    global connection, cursor

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
    connection.commit()

    return

def main():
    global connection, cursor
    
    path = ''
    connect(path)
    define_tables()
    
    connection.commit()
    connection.close()
    return

if __name__ == "__main__":
    main()