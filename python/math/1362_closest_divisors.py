import math


class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        n1, n2 = num + 1, num + 2
        r1, r2 = [], []
        for i in range(1, int(math.sqrt(n2)) + 1):
            if n1 % i == 0:
                r1 = [i, n1 // i]
            if n2 % i == 0:
                r2 = [i, n2 // i]
        if r1[1] - r1[0] <= r2[1] - r2[0]:
            return r1
        return r2


def test_closest_divisors():
    s = Solution()
    assert [3, 3] == s.closestDivisors(8)
    assert [5, 25] == s.closestDivisors(123)
    assert [25, 40] == s.closestDivisors(999)
