#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s1 = 1
        s2 = 0
        while n != 0:
            s1 = s1 * (n%10)
            s2 = s2 + (n%10)
            n = (int)(n / 10)
        return s1 - s2
# @lc code=end

