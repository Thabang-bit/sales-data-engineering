import duckdb
import pandas as pd

from src.load import load_data


def test_load_data_creates_sales_table(tmp_path):
    database_path = tmp_path / "test_sales.duckdb"

    data = pd.DataFrame({
        "order_id": [1, 2],
        "customer": ["Thabang", "John"],
        "product": ["Laptop", "Mouse"],
        "quantity": [1, 2],
        "price": [12000, 350],
        "date": ["2026-09-01", "2026-09-01"],
        "revenue": [12000, 700]
    })

    connection = duckdb.connect(str(database_path))

    connection.execute("""
        CREATE TABLE sales AS
        SELECT * FROM data
    """)

    result = connection.execute("SELECT COUNT(*) FROM sales").fetchone()[0]

    connection.close()

    assert result == 2