--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--

-- @lc code=start
# Write your MySQL query statement below
select FirstName, LastName, City, State
From Person left join address on Person.PersonId = address.PersonId
-- @lc code=end

