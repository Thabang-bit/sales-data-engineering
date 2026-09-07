import logging

from extract import extract_data
from transform import transform_data
from load import load_data


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def main():
    logging.info("Starting sales data pipeline")

    # Extract
    df = extract_data()
    logging.info("Extracted %d rows", len(df))

    # Transform
    clean_df = transform_data(df)
    logging.info("Transformed data: %d rows remaining", len(clean_df))

    # Load
    load_data(clean_df)
    logging.info("Data successfully loaded into DuckDB")

    logging.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()