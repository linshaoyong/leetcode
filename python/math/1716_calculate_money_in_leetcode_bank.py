class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, y, s = n // 7, n % 7, 0

        for i in range(x):
            s += 28 + i * 7

        for i in range(y):
            s += i + 1 + x
        return s


def test_total_money():
    s = Solution()
    assert 10 == s.totalMoney(4)
    assert 37 == s.totalMoney(10)
    assert 96 == s.totalMoney(20)
