class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        s = 0
        for i in range(len(dp[0])):
            dp[0][i] = s + grid[0][i]
            s = dp[0][i]
        s = 0
        for i in range(len(dp)):
            dp[i][0] = s + grid[i][0]
            s = dp[i][0]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


def test_min_path_sum():
    s = Solution()
    assert 7 == s.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ])

    assert 6 == s.minPathSum([[1, 2, 5], [3, 2, 1]])
