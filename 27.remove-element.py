#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ix = 0
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ix] = nums[i]
                ix+=1
        return ix
# @lc code=end

