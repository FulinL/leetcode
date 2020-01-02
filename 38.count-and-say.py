#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        ans = self.countAndSay(n-1) + '*'
        count = 1
        s = ""
        for i in range(len(ans)-1):
            if ans[i]==ans[i+1]:
                count+=1
            else:
                s = s + str(count) + str(ans[i])
                count=1
        return s
# @lc code=end

