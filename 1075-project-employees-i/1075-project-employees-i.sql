# Write your MySQL query statement below
select project.project_id , round(avg(employee.experience_years), 2) as average_years 
from project
join employee
on project.employee_id = employee.employee_id
group by project.project_id