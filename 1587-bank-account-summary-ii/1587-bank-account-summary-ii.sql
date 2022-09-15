# Write your MySQL query statement below
select u.name, sum(t.amount) as balance
from users u
join transactions t on t.account = u.account
group by u.account
having balance > 10000
