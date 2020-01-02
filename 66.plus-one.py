#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for x in digits:
            s = s * 10 + x
        s += 1
        res = []
        while s:
            res.append(s % 10)
            s = s // 10
        return res[::-1]
# @lc code=end

