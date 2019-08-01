class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        rs, cs = set(), set()
        for i in range(0, rows):
            for j in range(0, columns):
                if matrix[i][j] == 0:
                    rs.add(i)
                    cs.add(j)

        for i in range(0, rows):
            for j in range(0, columns):
                if i in rs or j in cs:
                    matrix[i][j] = 0


def test_set_zeroes():
    m = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    Solution().setZeroes(m)
    assert m == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]

    m = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(m)
    assert m == [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]
