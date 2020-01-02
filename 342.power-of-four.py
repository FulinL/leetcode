#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        return int(math.log(num, 4)) == math.log(num, 4)
# @lc code=end

