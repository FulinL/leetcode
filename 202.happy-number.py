#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    have = {}
    def isHappy(self, n: int) -> bool:
        if n in self.have.keys():
            self.have.clear()
            return False
        self.have[n] = 1
        if n == 1:
            self.have.clear()
            return True
        num = 0
        while n!=0:
            num+=(n%10)*(n%10)
            n/=10
            n = int(n)
        return self.isHappy(num)
# @lc code=end

