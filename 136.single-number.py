#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
import math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
# @lc code=end

