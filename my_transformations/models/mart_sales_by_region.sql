select
    region,
    category,
    count(distinct order_id) as total_orders,
    sum(sales) as total_sales,
    sum(profit) as total_profit,
    round(sum(profit) / nullif(sum(sales), 0) * 100, 2) as profit_margin_pct
from {{ ref('stg_orders') }}
group by region, category
order by total_sales desc