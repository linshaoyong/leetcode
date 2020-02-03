import math


class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        i, k, n = -1, 0, num
        while n:
            if n % 10 == 6:
                i = k
            k += 1
            n = n // 10
        return num + int(math.pow(10, i)) * 3 if i >= 0 else num


def test_maximum_69number():
    s = Solution()
    assert 9969 == s.maximum69Number(9669)
    assert 9999 == s.maximum69Number(9996)
    assert 9999 == s.maximum69Number(9999)
