class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and \
            [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


def test_spiral_order():
    s = Solution()

    assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == s.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    assert [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] == s.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
