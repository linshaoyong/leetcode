class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        m = 0
        min_v, max_v = prices[0], 0
        for p in prices[1:]:
            if p < min_v:
                m = max(max_v - min_v, m)
                min_v = p
                max_v = 0
                continue
            if p > max_v:
                max_v = p
        return max(max_v - min_v, m)


def test_max_profit():
    s = Solution()
    assert 5 == s.maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == s.maxProfit([7, 6, 4, 3, 1])
