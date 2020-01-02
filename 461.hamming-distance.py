#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x != 0 or y != 0:
            p = x%2
            q = y%2
            x = x // 2
            y = y // 2
            if p != q:
                res = res + 1
        return res
# @lc code=end

