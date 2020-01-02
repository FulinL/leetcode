#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range (0, numRows):
            res.append([1])
            for j in range (1, i+1):
                if j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j] + res[i-1][j-1])
        return res
# @lc code=end

