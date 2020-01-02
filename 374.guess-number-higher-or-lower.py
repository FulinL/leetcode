#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = l + (r - l) // 2
            res = guess(m)
            if res < 0:
                r = m - 1
            elif res > 0:
                l = m + 1
            else:
                return m
        return l
# @lc code=end

