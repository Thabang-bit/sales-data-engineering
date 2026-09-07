import pandas as pd

from src.transform import transform_data


def test_transform_removes_missing_values():
    data = pd.DataFrame({
        "order_id": [1, 2, 3],
        "customer": ["Thabang", "John", None],
        "product": ["Laptop", "Mouse", "Keyboard"],
        "quantity": [1, 2, 1],
        "price": [12000, 350, 800],
        "date": ["2026-09-01", "2026-09-01", "2026-09-02"]
    })

    result = transform_data(data)

    assert len(result) == 2
    assert result["customer"].isna().sum() == 0
    
def test_transform_calculates_revenue():
    data = pd.DataFrame({
        "order_id": [1],
        "customer": ["Thabang"],
        "product": ["Laptop"],
        "quantity": [2],
        "price": [12000],
        "date": ["2026-09-01"]
    })

    result = transform_data(data)

    assert result.iloc[0]["revenue"] == 24000
    
def test_transform_empty_dataframe():
    data = pd.DataFrame(columns=[
        "order_id",
        "customer",
        "product",
        "quantity",
        "price",
        "date"
    ])

    result = transform_data(data)

    assert result.empty
    assert "revenue" in result.columns    