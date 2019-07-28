class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        v = 0
        for i in range(3, n + 1):
            v = a + b
            a, b = b, v
        return v


def test_climb_stairs():
    s = Solution()

    assert 1 == s.climbStairs(1)
    assert 2 == s.climbStairs(2)
    assert 3 == s.climbStairs(3)
    assert 5 == s.climbStairs(4)
    assert 8 == s.climbStairs(5)
