1. Find the employees with the top 2 salaries in the company

```sql
select * 
from employee
where salary in (
  select max(salary)
  from employee
  where salary not in (
    select max(salary)
    from employee
  )
);
```

2. Find all supervisor names with the names of their second level supervisees

```sql
select * from employee as e
  join employee as s on e.ssn = s.super_ssn
where e not in (
  select * from employee as e
    join employee as s on e.ssn = s.super_ssn
  where e not in 
)

select * from employee as e, employee as s1, emplyoee as s2
where e,super_ssn = s2.ssn and s2.super_ssn = s1.ssn
```

3. Find the employees and the average number of hours they work on projects that are located in the same place as the departments that control them.

```sql
select *, avg(w.hours) avg_hours
from employee as e, works_on as w, project as p, dept_locations as d
where p.pnumber = w.pno and e.ssn = w.essn and p.plocation = d.dlocation
```

4. f

```sql
select *
from employee as e, project as p, department as d, works_on as w
where e.ssn = w.essn and p.dnum = e.dno and w.pno = p.pnumber


select * from employee
where not exists (
  select * from project where dnum = dno and not exists (select * from works_on where essn = ssn)
)

intersect

select *
from employee as e, emplyee as s, works_on as w1
where e.ssn = s.super_ssn and w1.essn = s.ssn and sw.pno not in (
  select w2.pno from works_on w2 where w2.essn = e.ssn
)
```
