# Write your MySQL query statement below
select a.customer_number as customer_number
from (
    select customer_number, count(order_number) as order_count
    from orders
    group by customer_number
) as a
order by a.order_count desc
limit 1
