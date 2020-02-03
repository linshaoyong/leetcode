class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [triangle[0][0]]
        for row in triangle[1:]:
            ndp = []
            for i in range(len(row)):
                if i == 0:
                    ndp.append(dp[i] + row[i])
                elif i == len(row) - 1:
                    ndp.append(dp[-1] + row[i])
                else:
                    ndp.append(min(dp[i], dp[i - 1]) + row[i])
            dp = ndp
        return min(dp)


def test_minimum_total():
    s = Solution()
    assert 11 == s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
