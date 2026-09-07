1. Project overview
2. Pipeline architecture
3. Technologies used
4. Project structure
5. How to run it
6. Example SQL analysis
7. What you learned

# Sales Data Engineering Pipeline

A beginner-friendly data engineering project that demonstrates a complete data pipeline using Python, Pandas, DuckDB, and SQL.

## Project Overview

This project takes raw sales data from a CSV file, cleans and transforms the data using Python and Pandas, stores the processed data in DuckDB, and uses SQL to analyse the results.

## Data Pipeline

```text
Raw CSV
   ↓
Extract
   ↓
Validate
   ↓
Transform
   ↓
DuckDB
   ↓
SQL Analysis
Technologies Used
Python
Pandas
DuckDB
SQL
Git
GitHub
Project Structure
sales-data-engineering/
│
├── data/
│   └── orders.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── query.py
│
├── sql/
│   └── analysis.sql
│
├── .gitignore
├── requirements.txt
└── README.md
How It Works
1. Extract

The extract.py module reads the raw sales data from the CSV file using Pandas.

2. Validate

The `validate.py` module checks that the required columns exist and that sales quantities and prices are greater than zero.

Invalid data is rejected before it reaches the transformation and loading stages.

3. Transform

The transform.py module:

Removes rows with missing values
Calculates revenue for each order

Revenue is calculated using:

revenue = quantity × price
4. Load

The load.py module loads the cleaned data into a DuckDB database.

5. Analyse

SQL queries are used to analyse the sales data, including:

Total revenue
Revenue by product
Revenue by customer
All processed sales
How to Run

Install the dependencies:

pip install -r requirements.txt

Run the data pipeline:

py src/pipeline.py

Run the SQL analysis:

py src/query.py
What I Learned

This project helped me practise:

Extracting data from CSV files
Cleaning and transforming data with Pandas
Loading data into a database
Writing SQL queries
Building an ETL pipeline
Organising a data engineering project
Using Git and GitHub for version control
Future Improvements

Planned improvements include:

Add automated tests
Add more realistic sales data
Add data validation
Add logging
Automate the pipeline
Create a data visualisation dashboard
