import duckdb
import pandas as pd


connection = duckdb.connect("sales.duckdb")

raw_data = pd.read_csv("data/orders.csv")

raw_records = len(raw_data)

clean_records = connection.execute("""
    SELECT COUNT(*)
    FROM sales
""").fetchone()[0]

removed_records = raw_records - clean_records


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
print("\nDATA QUALITY")
print("====================")
print(f"Raw records: {raw_records}")
print(f"Clean records: {clean_records}")
print(f"Removed records: {removed_records}")

print("\nREVENUE BY PRODUCT")
print("====================")

products = connection.execute("""
    SELECT
        product,
        SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC
""").fetchall()

for product, revenue in products:
    print(f"{product}: R{revenue:,.2f}")


connection.close()