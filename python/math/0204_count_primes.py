import math


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        厄拉多塞筛法
        比如求20以内质数的个数, 首先0,1不是质数。
        2是第一个质数,然后把20以内所有2的倍数划去。
        2后面紧跟的数即为下一个质数3，然后把3所有的倍数划去。
        3后面紧跟的数即为下一个质数5，再把5所有的倍数划去，以此类推。
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * int((n - i * i - 1) / i + 1)
        return sum(s)


def test_count_primes():
    s = Solution()
    assert 4 == s.countPrimes(10)
