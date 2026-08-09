import duckdb

conn = duckdb.connect(r"C:\elt-project\customers_pipeline.duckdb")
result = conn.sql("SELECT * FROM main.mart_sales_by_region").df()
print(result.to_string())