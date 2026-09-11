import pandas as pd

def extract_data():
    #reads our CSV file and turns it into a Pandas DataFrame
    df = pd.read_csv("data/orders.csv")
    return df