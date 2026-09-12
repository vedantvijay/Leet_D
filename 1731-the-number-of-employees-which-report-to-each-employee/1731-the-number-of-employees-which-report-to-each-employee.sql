# Write your MySQL query statement below
select 
    mgr.employee_id,
    mgr.name,
    count(emp.reports_to) as reports_count,
    round(avg(emp.age)) as average_age
from Employees mgr
JOIN Employees emp on mgr.employee_id = emp.reports_to
group by emp.reports_to
order by employee_id 