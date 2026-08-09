# Open-Source ELT Pipeline

A fully open-source ELT (Extract, Load, Transform) pipeline built as a local, cost-free alternative to cloud warehouses like Snowflake and Azure Synapse — using the same architectural pattern with `dlt`, DuckDB, and `dbt`.

## What it does

- **Extract & Load**: Ingests a real-world retail dataset (~10,000 rows, the classic Superstore sales dataset) using [`dlt`](https://dlthub.com/), landing raw data into a DuckDB warehouse.
- **Transform**: Uses [`dbt`](https://www.getdbt.com/) to build staging models that clean and normalize the raw data, then a business-facing mart aggregating total sales, profit, and profit margin by region and product category.
- **Test**: Automated dbt data tests (`not_null`, `unique`) validate data integrity on every run — 7/7 passing.

## Stack

| Layer | Tool |
|---|---|
| Extract & Load | [dlt](https://dlthub.com/) |
| Warehouse | [DuckDB](https://duckdb.org/) |
| Transform | [dbt](https://www.getdbt.com/) (dbt-duckdb adapter) |
| Language | Python 3.13 |

## Project structure

```
elt-project/
├── pipeline.py
├── customers_pipeline.duckdb
└── my_transformations/
    ├── models/
    │   ├── stg_customers.sql
    │   ├── stg_orders.sql
    │   ├── mart_sales_by_region.sql
    │   └── schema.yml
    └── dbt_project.yml
```

## Key finding

The pipeline surfaced a real business insight from the raw data: the **Central region's Office Supplies category has a -1.75% profit margin** despite over $167K in sales — a segment losing money that would be worth investigating further.

## Why local/open-source instead of cloud

This project intentionally swaps Snowflake/Synapse for DuckDB to keep the pipeline free to run and fully reproducible without cloud credentials. The transformation logic (dbt models, tests) is portable — the same SQL would run against Snowflake or Synapse with only the adapter and connection config changed.

## Running it

```bash
pip install dlt duckdb dbt-duckdb
python pipeline.py          # extract + load
cd my_transformations
dbt run                     # transform
dbt test                    # validate
```
