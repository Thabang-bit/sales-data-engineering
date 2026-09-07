def transform_data(df):
    # Remove rows with missing values
    df = df.dropna()

    # Calculate revenue
    df["revenue"] = df["quantity"] * df["price"]

    return df