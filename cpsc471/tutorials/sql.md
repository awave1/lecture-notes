1. Find the total number of kids whose GP is higher than 3.5 but only those who belong to schools with more than 20 students

```sql
select s.name, count(*) as no_students
from school as s, kid as k
where k.sname = s.name and
      k.gpa > 3.5 and
      s.name in (
        select k2.sname
        from kid as k2
        group by k2.sname
        having count (*) > 20
      )
```

2. Find names of all employees with employees who either work in finance dep or manage finance dep

```sql
select fname, lname
from employee, department, works_on
where employee.sin = works_on.sin and
      works_on.dno = department.no and
      department.name = 'finance'
union
select fname, lname
from employee, department
where employee.sin = department.mgr_sin and
      dep.name = 'finance'
```

3. Find names of employees who work for all departments
(divide by all departments)
```sql
select fname, lname
from employee
where (
  select dno
  from employee as e, works_on as w
  where e.sin = sin and
        w.sin = e.sin
)

```
