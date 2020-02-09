from math import factorial


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        nps = 0
        for i in range(2, n + 1):
            if self.is_prime(i):
                nps += 1
        return (factorial(nps) * factorial(n - nps)) % (10**9 + 7)

    def is_prime(self, n):
        for i in range(2, n // 2 + 1):
            if (n % i) == 0:
                return False
        return True


def test_num_prime_arrangements():
    s = Solution()
    assert 1 == s.numPrimeArrangements(2)
    assert 12 == s.numPrimeArrangements(5)
    assert 682289015 == s.numPrimeArrangements(100)
