#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strs = str.split(' ')
        if len(strs) != len(pattern):
            return False
        p = {}
        for c,s in zip(pattern, strs):
            if c not in p.keys():
                p[c] = s
                continue
            if p[c] != s:
                return False
        return True
# @lc code=end

