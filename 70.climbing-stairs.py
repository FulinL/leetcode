#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res = {}
        res[0] = 1
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]
# @lc code=end

