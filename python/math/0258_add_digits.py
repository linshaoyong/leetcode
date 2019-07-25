class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        v = 0
        while num > 0:
            v += num % 10
            num = num // 10
            if num == 0 and v > 9:
                num, v = v, 0

        return v


def test_add_digits():
    s = Solution()

    assert 2 == s.addDigits(38)
