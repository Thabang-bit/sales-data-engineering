import pandas as pd


def extract_data():
    df = pd.read_csv("data/orders.csv")
    return df