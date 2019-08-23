class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """


def test_is_power_of_four():
    s = Solution()
    assert s.isPowerOfFour(16)
    assert s.isPowerOfFour(5) is False
