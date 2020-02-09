class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        m, n = 1, num
        while True:
            n = n - m
            if n == 0:
                return True
            if n < 0:
                return False
            m += 2


def test_is_perfect_square():
    s = Solution()
    assert s.isPerfectSquare(16)
    assert s.isPerfectSquare(14) is False
    assert s.isPerfectSquare(2147483647) is False
