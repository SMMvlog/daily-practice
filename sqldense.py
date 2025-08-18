# SELECT id, name, dep_id, salary
# 	FROM public.employees;

# select dep_id,max(salary) from employees group by dep_id;

# select e.* from employees e join (select dep_id,max(salary) as mx_salary from employees group by dep_id) m on e.dep_id = m.dep_id where e.salary = m.mx_salary;

#  select e.* from employees e join (select salary,dep_id, Dense_rank() over(partition by dep_id order by salary desc) as sal_rank from employees) m
#  on e.dep_id=m.dep_id and e.salary=m.salary where m.sal_rank =3;

#  select *,dense_Rank() over(order by salary desc) as em_by_sal from employees;


# select * FROM users;

# select u.*,u1.* from users u inner join users u1 on u.email_id=u1.email_id;

# delete u1 from users u join users u1 on u.email_id=u1.email_id and u1.id >u.id;


# delete from users where id in (select u1.id from users u1 join users u on u1.email_id = u.email_id and u1.id < u.id);

# select * from users u1 join users u on u1.email_id = u.email_id ;


# select * from users2;

# select count(email_id) as duplicate_email  from users2 group by email_id having count(email_id) >1;

# select u.*,u1.* from users2 u join users2 u1 on u.email_id = u1.email_id;


# select * from employees;
# select left(cast(mobile_number as text),length(mobile_number)-4) || 'xxxx' as encrypted_mobile_number from employee_master;





