class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        b = bin(num)
        return num > 0 and b.count("1") == 1 and \
            (len(b) - b.index("1")) % 2 == 1


def test_is_power_of_four():
    s = Solution()
    assert s.isPowerOfFour(16)
    assert s.isPowerOfFour(2) is False
    assert s.isPowerOfFour(5) is False
