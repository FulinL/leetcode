#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        px = nums[0]
        p = 1
        for i in range (1, n):
            if nums[i] != px:
                nums[p] = nums[i]
                px = nums[i]
                p = p+1
        return p
# @lc code=end

