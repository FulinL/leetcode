--
-- @lc app=leetcode id=178 lang=mysql
--
-- [178] Rank Scores
--

-- @lc code=start
# Write your MySQL query statement below
select Score,
(
    select count(distinct Score)
    from Scores
    where Score >= s.Score
) as Rank
from Scores s
order by Score desc

-- @lc code=end

