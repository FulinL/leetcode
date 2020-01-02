#
# @lc app=leetcode id=1078 lang=python3
#
# [1078] Occurrences After Bigram
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s = text.split(' ')
        n = len(s)
        res = []
        for i in range(n-2):
            if i < n - 2:
                if s[i] == first and s[i+1] == second:
                    res.append(s[i+2])
        return res
# @lc code=end

