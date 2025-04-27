# Write your MySQL query statement below

select
    today.id
from
    Weather today
join
    Weather yesterday
ON
    DATEDIFF(today.recordDate, yesterday.recordDate) = 1
where
    today.temperature > yesterday.temperature