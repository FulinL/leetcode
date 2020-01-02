#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        mxsum = nums[0]
        for num in nums:
            sum += num
            mxsum = max(sum, mxsum)
            if sum <= 0:
                sum=0
        return mxsum
# @lc code=end

