# CMPUT-291-Assignment-3
GROUP #83
Name        | CCID
------------------------
Logan Jones | lajones
Raezan Villamor | raezan
Muhammad Hamza | mhamza2

We declare that we did not collaborate with anyone outside our own
group in this assignment other than those who are in the public discord server forums


Q1A3, Q2A3, Q3A3 User Optimized Scenarios are shared between the 3 of them

-------------------------------

c.execute("CREATE INDEX idx_customers_postal_code ON Customers(customer_postal_code);") --> Chosen since we are querying a random customers_postal code frequently as one of our parameters
c.execute("CREATE INDEX idx_orders_customer_id ON Orders(customer_id);") --> Since we're querying customer_id to get the random postal code of customer we decided that an index here would optimize our code
c.execute("CREATE INDEX idx_orders_order_id ON Orders(order_id);") --> Since we're checking if the customers order_id in order_items is greater than 1 we decided an index here was necessary
c.execute("CREATE INDEX idx_order_items_order_id ON Order_items(order_id);") --> Since we're also querying order_items in the subquery this will speed up the query with the index
c.execute("CREATE INDEX idx_order_items_order_item_id ON Order_items(order_item_id);") --> since we're grabbing order_it from Order_items this is pretty much reason as the one above



Q4A3 User Optimized Scenarios
NOTE: Similarities are from Q1, Q2, Q3 are here with the ones below being the extra indexes
-idx_order_items_seller_id
-idx_sellers_seller_id
-idx_sellers_seller_postal_code
-idx_customers_customer_id
-------------------------------
c.execute("CREATE INDEX idx_orders_customer_id ON Orders (customer_id);") --> Since we're querying customer_id to get the random postal code of customer we decided that an index here would optimize our code
c.execute("CREATE INDEX idx_order_items_order_id ON Order_items (order_id);") -->Since we're also querying order_items in the subquery this will speed up the query with the index
c.execute("CREATE INDEX idx_order_items_seller_id ON Order_items (seller_id);") --> Since we're grabbing the seller_id to check with the seller_id in order items and index here would speed up our time
c.execute("CREATE INDEX idx_sellers_seller_id ON Sellers (seller_id);") --> Same thing as the one above. Since we will eventually implicitly join them together
c.execute("CREATE INDEX idx_sellers_seller_postal_code ON Sellers (seller_postal_code);") --> Since we are finding the amount of DISTINCT sellers postal code for those who have more than 1 order
c.execute("CREATE INDEX idx_customers_customer_id ON Customers (customer_id);") --> The customers_id we decided to also index since we need it to correspond to the order of the customer and see if they have more than 1 order

IMPORTANT NOTE #1 FOR Q4:
Currently there is 1 customer who has more than 1 order in the given database with 2 distinct seller postal codes.
It is important to note that in the case that if you are using a different database with NO customers having > 1 orders uninformed WILL run faster than self-Optimized
Since we are doing a cartesian joins on the table.

IMPORTANT NOTE #2 FOR Q4:
We are doing joins with the cartesian product the uninformed function for the given database will run
for 4 minutes until it can fully grab all of the information.

IMPORTANT NOTE #3 For all parts:
Instead of doing a stacked bar graph we have decided that a side by side bar chart would better convey
the information that uninformed > selfOptimized > userOptimized in all of the runtimes.
Q4's chart is heavily skewed for the charts and thus you may not be able to see the graph clearly for 
selfOptimized and userOptimized but they are there.

Adding on to the note above we have also decided to output the running times of the 50 times the functions
will run to also see that uninformed > selfOptimized > userOptimized in terms of runtimes to make it easiter for the markers
