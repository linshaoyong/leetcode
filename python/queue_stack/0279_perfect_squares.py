class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """


def test_num_squares():
    s = Solution()
    assert 3 == s.numSquares(12)
    assert 2 == s.numSquares(13)
