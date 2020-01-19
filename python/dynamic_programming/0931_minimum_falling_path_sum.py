class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp = A[0]
        for i in range(1, len(A)):
            ndp = []
            for j in range(len(dp)):
                prevs = [dp[j]]
                if j > 0:
                    prevs.append(dp[j - 1])
                if j < len(dp) - 1:
                    prevs.append(dp[j + 1])
                ndp.append(min(prevs) + A[i][j])
            dp = ndp
        return min(dp)


def test_min_falling_path_sum():
    s = Solution()
    assert 12 == s.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
