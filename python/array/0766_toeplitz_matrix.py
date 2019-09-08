class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(0, m):
            for j in range(0, n):
                if i < m - 1 and j < n - 1 and \
                        matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


def test_is_toeplitz_matrix():
    assert Solution().isToeplitzMatrix([
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ])

    assert Solution().isToeplitzMatrix([
        [1, 2],
        [2, 2]
    ]) is False
