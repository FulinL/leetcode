#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        p = []
        for x,y in zip(s, t):
            if x not in m.keys():
                m[x] = y
                if y in p:
                    return False
                else:
                    p.append(y)
            if m[x] != y:
                return False
        return True
# @lc code=end

