#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        p = strs[0]
        for i in range(1, n):
            while strs[i].find(p) != 0:
                p = p[:len(p)-1]
                if p == "":
                    return p
        return p
# @lc code=end

