select employee_id, IF(NOT name LIKE "M%" AND MOD(employee_id,2) = 1, salary, 0) as bonus
from Employees
order by employee_id;