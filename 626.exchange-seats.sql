--
-- @lc app=leetcode id=626 lang=mysql
--
-- [626] Exchange Seats
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
    (CASE 
     WHEN MOD(id,2)!=0 AND id != counts THEN id+1
     WHEN MOD(id,2)!=0 AND id = counts THEN id
     ELSE id-1
     END
    ) AS id, student 
FROM seat, (SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id;
-- @lc code=end

