import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(1 + 8 * n) - 1) // 2)


def test_arrange_coins():
    s = Solution()
    assert 2 == s.arrangeCoins(5)
    assert 3 == s.arrangeCoins(8)
