class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        while n > 0:
            if n % 2 == 1:
                s += 1
            n = n // 2
        return s


def test_0():
    assert Solution().hammingWeight(11) == 3
    assert Solution().hammingWeight(128) == 1
