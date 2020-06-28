class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res = [0] * len(prices)
        for i in range(len(prices)):
            res[i] = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res


def test_final_prices():
    s = Solution()
    assert [4, 2, 4, 2, 3] == s.finalPrices([8, 4, 6, 2, 3])
    assert [1, 2, 3, 4, 5] == s.finalPrices([1, 2, 3, 4, 5])
    assert [9, 0, 1, 6] == s.finalPrices([10, 1, 1, 6])
