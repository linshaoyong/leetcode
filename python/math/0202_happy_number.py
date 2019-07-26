class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set([n])
        v = 0
        while n > 0:
            m = n % 10
            n = n // 10
            v += m * m
            if n == 0:
                if v == 1:
                    return True
                if v in s:
                    return False
                n, v = v, 0
                s.add(n)


def test_is_happy():
    s = Solution()
    assert s.isHappy(19) is True
    assert s.isHappy(2) is False
    assert s.isHappy(7) is True
    assert s.isHappy(1111111) is True
