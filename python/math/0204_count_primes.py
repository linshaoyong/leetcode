import math


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
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
