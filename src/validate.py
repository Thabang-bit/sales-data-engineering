REQUIRED_COLUMNS = [
    "order_id",
    "customer",
    "product",
    "quantity",
    "price",
    "date"
]


def validate_data(df):
    # Check required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check quantity and price
    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than 0")

    if (df["price"] <= 0).any():
        raise ValueError("Price must be greater than 0")
    
        # Check for duplicate order IDs
    if df["order_id"].duplicated().any():
        raise ValueError("Order IDs must be unique")

    return True