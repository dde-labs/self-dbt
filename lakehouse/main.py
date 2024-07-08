import duckdb

conn = duckdb.connect(database='./dev.duckdb', read_only=False)
query = (
    "SELECT table_name "
    "FROM information_schema.tables WHERE table_schema='main';"
)
tables = conn.execute(query).fetchall()

for table in tables:
    print(table[0])

query = "SELECT * FROM my_first_dbt_model LIMIT 1;"
example_row = conn.execute(query).fetchall()
print(example_row)
