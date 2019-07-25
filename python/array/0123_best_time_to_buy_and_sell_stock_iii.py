class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return 0


def test_max_profit():
    s = Solution()

    assert 6 == s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
    assert 4 == s.maxProfit([1, 2, 3, 4, 5])
    assert 13 == s.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
