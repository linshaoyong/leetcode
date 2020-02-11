class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        v = 0
        prev = prices[0]
        for num in prices[1:]:
            if num > prev:
                v += num - prev
            prev = num
        return v


def test_max_profit():
    s = Solution()

    assert 7 == s.maxProfit([7, 1, 5, 3, 6, 4])
    assert 4 == s.maxProfit([1, 2, 3, 4, 5])
    assert 0 == s.maxProfit([7, 6, 4, 3, 1])
    assert 7 == s.maxProfit([3, 2, 6, 5, 0, 3])
