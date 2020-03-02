class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        profits, start = [], prices[0]
        for i in range(1, len(prices) + 1):
            current = 0 if i == len(prices) else prices[i]
            if current < prices[i - 1]:
                if prices[i - 1] > start:
                    profits.append([start, prices[i - 1]])
                start = current

        res = 0
        return res


def test_max_profit():
    s = Solution()
    assert 8 == s.maxProfit([1, 3, 2, 8, 4, 9], 2)
