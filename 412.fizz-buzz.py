#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            s = ""
            if i % 3 == 0:
                s = s + "Fizz"
            if i % 5 == 0:
                s = s + "Buzz"
            if i % 3 != 0 and i % 5 != 0:
                s = str(i)
            res.append(s)
        return res
# @lc code=end

