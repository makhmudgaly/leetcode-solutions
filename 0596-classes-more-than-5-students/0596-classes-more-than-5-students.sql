# Write your MySQL query statement below
select class
from (
    select class, count(student) as num
    from courses
    group by class
) as a
where a.num > 4

