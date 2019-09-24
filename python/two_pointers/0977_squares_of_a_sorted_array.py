class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        v = sorted([abs(i) for i in A])
        return [i * i for i in v]


def test_sorted_squares():
    s = Solution()
    assert [0, 1, 9, 16, 100] == s.sortedSquares([-4, -1, 0, 3, 10])
    assert [4, 9, 9, 49, 121] == s.sortedSquares([-7, -3, 2, 3, 11])
