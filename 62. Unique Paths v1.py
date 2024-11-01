class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0] * (n+1)] * (m+1)
        for j in range(1,m+1):
            for i in range(1,n+1):
                if i == 1 and j == 1:
                    ans[j][i] = 1
                else:
                    ans[j][i] = ans[j-1][i] + ans[j][i-1]
        return ans[m][n]
