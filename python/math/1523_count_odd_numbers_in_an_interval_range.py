class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        n = high - low + 1
        return n // 2 if low % 2 == 0 else 1 + (n - 1) // 2


def test_countOdds():
    s = Solution()
    assert 3 == s.countOdds(3, 7)
    assert 1 == s.countOdds(8, 10)
    assert 1 == s.countOdds(21, 22)
