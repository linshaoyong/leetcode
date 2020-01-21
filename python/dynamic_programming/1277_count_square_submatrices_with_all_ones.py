class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i - 1][j - 1],
                                       dp[i - 1][j], dp[i][j - 1]) + 1
                    else:
                        dp[i][j] = 1
        return sum([sum(r) for r in dp])


def test_count_squares():
    s = Solution()
    assert 15 == s.countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ])

    assert 7 == s.countSquares([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ])
