def transform_data(df):
    # Remove rows with missing values
    df = df.dropna()
    
    # Keep only valid sales remove invalid sales.
    df = df[(df["quantity"] > 0) & (df["price"] > 0)]

    # Calculate revenue mean creates a new column.
    df["revenue"] = df["quantity"] * df["price"]

    return df

#this change raw data to clean data.