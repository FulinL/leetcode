--
-- @lc app=leetcode id=596 lang=mysql
--
-- [596] Classes More Than 5 Students
--

-- @lc code=start
# Write your MySQL query statement below
select class
from courses
group by class
having count(distinct student) > 4
-- @lc code=end

