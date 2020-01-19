class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            ccs = [dp[i - coin] + 1 for coin in coins if i >=
                   coin and dp[i - coin] >= 0]
            if ccs:
                dp[i] = min(ccs)
        return dp[-1]


def test_coin_change():
    s = Solution()
    assert 3 == s.coinChange([1, 2, 5], 11)
    assert -1 == s.coinChange([2], 3)
