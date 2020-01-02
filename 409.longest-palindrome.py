#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        f = 0
        res = 0
        for c in s:
            if c not in m.keys():
                m[c] = 1
            else:
                m[c] += 1
                if m[c] == 2:
                    f -= 1
                    res += 1
                    m[c] = 0
            if m[c] == 1:
                f += 1
        res = res * 2
        if f > 0:
            res += 1
        return res
# @lc code=end

