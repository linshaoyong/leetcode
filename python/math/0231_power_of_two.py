class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return (n & (n - 1)) == 0


def test_is_power_of_two():
    s = Solution()
    assert s.isPowerOfTwo(1) is True
    assert s.isPowerOfTwo(16) is True
    assert s.isPowerOfTwo(218) is False
