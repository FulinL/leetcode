#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[] for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                    continue
                res[i].append(res[i-1][j] + res[i-1][j-1])
        return res[rowIndex]
# @lc code=end

