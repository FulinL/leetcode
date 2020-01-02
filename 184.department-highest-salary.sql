--
-- @lc app=leetcode id=184 lang=mysql
--
-- [184] Department Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below
select Department.Name as Department, Employee.Name as Employee, Employee.Salary as Salary
from Employee left join Department on Employee.DepartmentId = Department.Id
right join 
(
    select DepartmentId, max(Salary) as Salary
    from Employee
    group by DepartmentId
) as s on s.DepartmentId = Employee.DepartmentId and s.Salary = Employee.Salary
where Department.Name is not null and Employee.Name is  not null and Employee.Salary is not null
-- @lc code=end

