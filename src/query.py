import duckdb


connection = duckdb.connect("sales.duckdb")


print("ALL SALES")
print(connection.execute("""
    SELECT *
    FROM sales
""").fetchdf())

# this ask how much money did we make?
print("\nTOTAL REVENUE")
print(connection.execute("""
    SELECT SUM(revenue) AS total_revenue
    FROM sales
""").fetchdf())

#to find revenue per product.
print("\nREVENUE BY PRODUCT")
print(connection.execute("""
    SELECT
        product,
        SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC
""").fetchdf())


print("\nREVENUE BY CUSTOMER")
print(connection.execute("""
    SELECT
        customer,
        SUM(revenue) AS total_spent
    FROM sales
    GROUP BY customer
    ORDER BY total_spent DESC
""").fetchdf())

print("\nORDER METRICS")
print(connection.execute("""
    SELECT
        COUNT(*) AS total_orders,
        SUM(revenue) AS total_revenue,
        AVG(revenue) AS average_order_value
    FROM sales
""").fetchdf())

print("\nDAILY REVENUE")
print(connection.execute("""
    SELECT
        date,
        SUM(revenue) AS daily_revenue
    FROM sales
    GROUP BY date
    ORDER BY date
""").fetchdf())

connection.close()