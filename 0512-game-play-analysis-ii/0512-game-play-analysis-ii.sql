-- Write your PostgreSQL query statement below
with preprocess as (
    select 
        player_id, 
        device_id,
        row_number() over(partition by player_id order by event_date) as rn
    from activity
)
select player_id, device_id
from preprocess
where rn = 1