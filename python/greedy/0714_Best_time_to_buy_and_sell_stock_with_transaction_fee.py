class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """


def test_max_profit():
    s = Solution()
    assert 8 == s.maxProfit([1, 3, 2, 8, 4, 9], 2)
