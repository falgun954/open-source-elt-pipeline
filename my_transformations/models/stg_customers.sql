select
    id as customer_id,
    name as customer_name,
    lower(email) as email,
    signup_date
from raw.customers