#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = abs(nums[i])
            if nums[x] < 0:
                return x
            else:
                nums[x] = -nums[x]
# @lc code=end

