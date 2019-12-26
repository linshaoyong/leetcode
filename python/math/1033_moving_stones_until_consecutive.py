class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        points = sorted([a, b, c])
        x, y = points[1] - points[0] - 1, points[2] - points[1] - 1
        low, hight = min(x, y), max(x, y)
        mn = 1
        if hight == 0:
            mn = 0
        if low > 1:
            mn = 2
        return [mn, low + hight]


def test_num_moves_stones():
    s = Solution()
    assert [1, 2] == s.numMovesStones(1, 2, 5)
    assert [0, 0] == s.numMovesStones(4, 3, 2)
    assert [1, 2] == s.numMovesStones(3, 5, 1)
