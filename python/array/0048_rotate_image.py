class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0, n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(0, n):
            for j in range(0, n // 2):
                matrix[i][j], matrix[i][n - 1 -
                                        j] = matrix[i][n - 1 - j], matrix[i][j]


def test_rotate_1():
    s = Solution()
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    s.rotate(m)
    assert m == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]


def test_rotate_2():
    s = Solution()
    m = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate(m)
    assert m == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
