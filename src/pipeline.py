from extract import extract_data
from transform import transform_data
from load import load_data


def main():
    # Extract
    df = extract_data()

    print("RAW DATA")
    print(df)

    # Transform
    clean_df = transform_data(df)

    print("\nCLEAN DATA")
    print(clean_df)

    # Load
    load_data(clean_df)

    print("\nData successfully loaded into database!")


if __name__ == "__main__":
    main()