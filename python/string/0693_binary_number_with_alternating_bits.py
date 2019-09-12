class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)[2:]
        prev = s[0]
        for c in s[1:]:
            if c == prev:
                return False
            prev = c
        return True


def test_has_alternating_bits():
    s = Solution()
    assert s.hasAlternatingBits(5)
    assert s.hasAlternatingBits(7) is False
    assert s.hasAlternatingBits(11) is False
    assert s.hasAlternatingBits(10)
