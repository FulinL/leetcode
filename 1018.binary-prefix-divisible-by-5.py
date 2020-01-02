#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        s = 0
        res = []
        for ix in A:
            s = s * 2 + ix
            if s % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
# @lc code=end

