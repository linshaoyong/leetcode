class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        m = 0
        min_v, max_v = prices[0], prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                if max_v - min_v > 0:
                    m += max_v - min_v
                min_v = prices[i]
                max_v = 0
                continue
            if prices[i] > max_v:
                max_v = prices[i]
        if max_v - min_v > 0:
            m += max_v - min_v
        return m


def test_max_profit():
    s = Solution()

    assert 7 == s.maxProfit([7, 1, 5, 3, 6, 4])
    assert 4 == s.maxProfit([1, 2, 3, 4, 5])
    assert 0 == s.maxProfit([7, 6, 4, 3, 1])
    assert 7 == s.maxProfit([3, 2, 6, 5, 0, 3])
