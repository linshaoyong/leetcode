class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        up = True
        n = len(matrix) * len(matrix[0])
        s = []
        for i in range(0, n):
            pass
        return s


def test_find_diagonal_order():
    s = Solution()
    assert [1, 2, 4, 7, 5, 3, 6, 8, 9] == s.findDiagonalOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
