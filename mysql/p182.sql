select email from (
    select count(email) as c, email from Person group by email
    ) as T
    where T.c > 1
