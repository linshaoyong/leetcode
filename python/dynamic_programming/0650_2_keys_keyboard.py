class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 0, 2, 3]
        if n <= 3:
            return dp[n]
        for i in range(4, n + 1):
            dp.append(float('inf'))
            j = 1
            while i >= j:
                if i % j == 0:
                    dp[i] = min(dp[i], dp[i // j] + j)
                j += 1
        return dp[-1]


def test_min_steps():
    s = Solution()
    assert 0 == s.minSteps(1)
    assert 2 == s.minSteps(2)
    assert 3 == s.minSteps(3)
    assert 4 == s.minSteps(4)
    assert 5 == s.minSteps(5)
    assert 6 == s.minSteps(9)
