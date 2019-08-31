class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        num = self.division(num, 2)
        num = self.division(num, 3)
        num = self.division(num, 5)
        return num == 0 or num == 1

    def division(self, num, factor):
        while num and num % factor == 0:
            num = num // factor
        return num


def test_is_ugly():
    assert Solution().isUgly(0) is False
    assert Solution().isUgly(1)
    assert Solution().isUgly(6)
    assert Solution().isUgly(8)
    assert Solution().isUgly(14) is False
