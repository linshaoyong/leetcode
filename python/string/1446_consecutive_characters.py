class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        power, p, prev = 1, 1, s[0]
        for c in s[1:]:
            if c == prev:
                p += 1
            else:
                power = max(power, p)
                p = 1
            prev = c
        return max(power, p)


def test_max_power():
    s = Solution()
    assert 2 == s.maxPower("leetcode")
    assert 5 == s.maxPower("abbcccddddeeeeedcba")
    assert 5 == s.maxPower("triplepillooooow")
    assert 11 == s.maxPower("hooraaaaaaaaaaay")
    assert 1 == s.maxPower("tourist")
