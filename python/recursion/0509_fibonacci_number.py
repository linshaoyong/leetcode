class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


def test_fib():
    s = Solution()
    assert 1 == s.fib(2)
    assert 2 == s.fib(3)
    assert 3 == s.fib(4)
