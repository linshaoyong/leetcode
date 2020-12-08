class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = 0
        rows, columns, j = len(mat[0]), len(mat[0]), 0
        for i in range(rows):
            res += mat[i][j]
            if columns - 1 - j != j:
                res += mat[i][columns - 1 - j]
            j += 1
        return res


def test_diagonal_sum():
    s = Solution()

    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    assert 25 == s.diagonalSum(mat)

    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    assert 8 == s.diagonalSum(mat)

    mat = [[5]]
    assert 5 == s.diagonalSum(mat)
