import duckdb


connection = duckdb.connect("sales.duckdb")

with open("sql/analysis.sql", "r") as file:
    sql = file.read()

results = connection.execute(sql).fetchall()

for row in results:
    print(row)

connection.close()