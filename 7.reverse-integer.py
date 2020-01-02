#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        while x !=0:
            ans = ans*10 + x%10
            x = x // 10
        if flag == 1:
            ans = -ans
        if ans > 2**31-1 or ans < -2**31:
            ans = 0
        return ans
# @lc code=end

