import duckdb

conn = duckdb.connect(r"C:\elt-project\customers_pipeline.duckdb")
result = conn.sql("SELECT * FROM main.stg_customers").df()
print(result)
