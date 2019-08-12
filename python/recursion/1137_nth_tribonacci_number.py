class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return [0, 1, 1][n]
        a, b, c = (0, 1, 1)
        for _ in range(3, n + 1):
            s = a + b + c
            a = b
            b = c
            c = s
        return c


def test_tribonacci():
    s = Solution()

    assert 0 == s.tribonacci(0)
    assert 1 == s.tribonacci(1)
    assert 1 == s.tribonacci(2)
    assert 2 == s.tribonacci(3)
    assert 4 == s.tribonacci(4)
    assert 7 == s.tribonacci(5)
