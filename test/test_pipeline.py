from src.extract import extract_data
from src.transform import transform_data
from src.validate import validate_data


def test_etl_pipeline():
    # Extract
    df = extract_data()

    # Validate
    assert validate_data(df) is True

    # Transform
    clean_df = transform_data(df)

    # Check that invalid/missing rows were removed
    assert len(clean_df) == 6

    # Check that revenue was calculated
    assert "revenue" in clean_df.columns

    # Check that all revenue values are positive
    assert (clean_df["revenue"] > 0).all()