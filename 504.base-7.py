#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        f = 1
        res = ""
        if num < 0:
            num = -num
            f = -1
        while num:
            res = res + str(num%7)
            num = num // 7
        if f != 1:
            res = res + "-"
        return res[::-1]
# @lc code=end

