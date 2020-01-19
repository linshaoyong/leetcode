class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 2, 3]
        if n <= 3:
            return dp[n]
        for i in range(4, n + 1):
            dp.append(float('inf'))
            j = 1
            while i >= j * j:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


def test_num_squares():
    s = Solution()
    assert 1 == s.numSquares(1)
    assert 2 == s.numSquares(2)
    assert 3 == s.numSquares(3)
    assert 1 == s.numSquares(4)
    assert 2 == s.numSquares(5)
    assert 3 == s.numSquares(12)
    assert 2 == s.numSquares(13)
