class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = []
        y = abs(x)
        while y > 0:
            s.append(y % 10)
            y = y // 10
        v = 0
        for i in range(0, len(s)):
            v += s[i] * (10**(len(s) - 1 - i))
        if x < 0:
            v = -v
        return 0 if v > 2147483647 or v < -2147483648 else v


def test_reverse():
    s = Solution()
    assert 321 == s.reverse(123)
    assert -321 == s.reverse(-123)
    assert 21 == s.reverse(120)
    assert 0 == s.reverse(1534236469)
