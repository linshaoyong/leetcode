class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """


def test_minimum_swap():
    s = Solution()
    assert 1 == s.minimumSwap("xx", "yy")
    assert 2 == s.minimumSwap("xy", "yx")
    assert -1 == s.minimumSwap("xx", "xy")
    assert 4 == s.minimumSwap("xxyyxyxyxx", "xyyxyxxxyx")
