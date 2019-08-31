class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0


def test_get_money_amount():
    assert 0 == Solution().getMoneyAmount(1)
    assert 1 == Solution().getMoneyAmount(2)
    assert 2 == Solution().getMoneyAmount(3)
    assert 4 == Solution().getMoneyAmount(4)
    assert 10 == Solution().getMoneyAmount(7)
    assert 21 == Solution().getMoneyAmount(10)
