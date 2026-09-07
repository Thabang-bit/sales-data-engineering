import duckdb
import pandas as pd


def load_data(df: pd.DataFrame):
    connection = duckdb.connect("sales.duckdb")

    connection.execute("""
        CREATE OR REPLACE TABLE sales AS
        SELECT * FROM df
    """)

    connection.close()