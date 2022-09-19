# Write your MySQL query statement below
select author_id as id
from (
    select author_id, count(article_id) as cnt
    from views
    where author_id = viewer_id
    group by author_id
    having cnt >= 1
) a
order by id asc
