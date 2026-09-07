import duckdb


connection = duckdb.connect("sales.duckdb")


result = connection.execute("""
    SELECT
        COUNT(*) AS total_orders,
        SUM(revenue) AS total_revenue,
        AVG(revenue) AS average_order_value
    FROM sales
""").fetchone()


total_orders = result[0]
total_revenue = result[1]
average_order_value = result[2]


print("SALES REPORT")
print("====================")
print(f"Total orders: {total_orders}")
print(f"Total revenue: R{total_revenue:,.2f}")
print(f"Average order value: R{average_order_value:,.2f}")


connection.close()