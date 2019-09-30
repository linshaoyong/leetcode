class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            m = n // 5
            res += m
            n = m
        return res


def test_trailing_zeros():
    s = Solution()
    assert 0 == s.trailingZeroes(3)
    assert 0 == s.trailingZeroes(0)
    assert 1 == s.trailingZeroes(5)
    assert 7 == s.trailingZeroes(30)
    assert 12 == s.trailingZeroes(50)
