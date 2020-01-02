#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            x = abs(nums[i])
            if nums[x-1] > 0:
                nums[x-1] = -nums[x-1]
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
# @lc code=end