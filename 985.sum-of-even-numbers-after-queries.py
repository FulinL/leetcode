#
# @lc app=leetcode id=985 lang=python3
#
# [985] Sum of Even Numbers After Queries
#

# @lc code=start
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        n = len(queries)
        sum = 0
        for x in A:
            if x % 2 == 0:
                sum += x
        for i in range(n):
            if A[queries[i][1]] % 2 == 0:
                if queries[i][0] % 2 == 0:
                    sum += queries[i][0]
                else:
                    sum -= A[queries[i][1]]
            else:
                if queries[i][0] % 2 != 0:
                    sum += queries[i][0]+A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
            res.append(sum)
        return res
# @lc code=end
