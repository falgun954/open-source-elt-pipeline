import dlt
import csv

with open("superstore.csv", newline="", encoding="latin-1") as f:
    reader = csv.DictReader(f)
    data = list(reader)

pipeline = dlt.pipeline(
    pipeline_name="customers_pipeline",
    destination="duckdb",
    dataset_name="raw"
)

load_info = pipeline.run(data, table_name="orders")
print(load_info)
print(f"Loaded {len(data)} rows")