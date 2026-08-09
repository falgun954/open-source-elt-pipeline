select
    row_id,
    order_id,
    cast(order_date as date) as order_date,
    customer_name,
    segment,
    region,
    category,
    sub_category,
    cast(sales as double) as sales,
    cast(quantity as integer) as quantity,
    cast(discount as double) as discount,
    cast(profit as double) as profit
from raw.orders