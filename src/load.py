import duckdb
import pandas as pd


def load_data(df: pd.DataFrame, database_path="sales.duckdb"):
    connection = duckdb.connect(database_path)

    connection.execute("""
        CREATE OR REPLACE TABLE sales AS
        SELECT * FROM df
    """)

    connection.close()