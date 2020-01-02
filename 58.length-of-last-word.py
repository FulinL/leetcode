#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s)-1
        res = 0
        while r >= 0 and s[r] == ' ':
            r = r - 1
        while r >= 0 and s[r] != ' ':
            r = r - 1
            res = res + 1
        return res

# @lc code=end

