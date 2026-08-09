import duckdb

conn = duckdb.connect("customers_pipeline.duckdb")
result = conn.sql("SELECT * FROM raw.customers").df()
print(result)