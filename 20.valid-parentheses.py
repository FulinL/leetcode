#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        peer = {}
        peer['('] = ')'
        peer['['] = ']'
        peer['{'] = '}'
        for c in s:
            if len(ans) == 0:
                ans.append(c)
                continue
            if ans[-1] in ['(','[','{']:
                if peer[ans[-1]] == c:
                    ans.pop()
                else:
                    ans.append(c)
            if len(ans) > 0 and ans[-1] in [')',']','}']:
                return False
        return len(ans) == 0
# @lc code=end

