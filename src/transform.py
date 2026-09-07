def transform_data(df):
    # Remove rows with missing values
    df = df.dropna()
    
    # Keep only valid sales
    df = df[(df["quantity"] > 0) & (df["price"] > 0)]

    # Calculate revenue
    df["revenue"] = df["quantity"] * df["price"]

    return df