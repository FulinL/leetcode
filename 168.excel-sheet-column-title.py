#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n != 0:
            p = n % 26
            if p == 0:
                p = 26
                n = n-26
                s = s + 'Z'
            else :
                s = s + chr(ord('A')+p-1)
            n = n // 26
        return s[::-1]
# @lc code=end

