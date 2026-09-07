import pandas as pd
import pytest

from src.validate import validate_data


def test_validate_data_accepts_valid_data():
    data = pd.DataFrame({
        "order_id": [1],
        "customer": ["Thabang"],
        "product": ["Laptop"],
        "quantity": [1],
        "price": [12000],
        "date": ["2026-09-01"]
    })

    assert validate_data(data) is True


def test_validate_data_rejects_negative_quantity():
    data = pd.DataFrame({
        "order_id": [1],
        "customer": ["Thabang"],
        "product": ["Laptop"],
        "quantity": [-1],
        "price": [12000],
        "date": ["2026-09-01"]
    })

    with pytest.raises(ValueError):
        validate_data(data)


def test_validate_data_rejects_missing_column():
    data = pd.DataFrame({
        "order_id": [1],
        "customer": ["Thabang"],
        "product": ["Laptop"],
        "quantity": [1],
        "price": [12000]
    })

    with pytest.raises(ValueError):
        validate_data(data)
        
def test_validate_data_rejects_duplicate_order_ids():
    data = pd.DataFrame({
        "order_id": [1, 1],
        "customer": ["Thabang", "John"],
        "product": ["Laptop", "Mouse"],
        "quantity": [1, 2],
        "price": [12000, 350],
        "date": ["2026-09-01", "2026-09-01"]
    })

    with pytest.raises(ValueError):
        validate_data(data)