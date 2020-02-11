class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mrow = [0] * len(grid)
        mcolumn = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                mrow[i] = max(mrow[i], grid[i][j])
                mcolumn[j] = max(mcolumn[j], grid[i][j])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res += min(mrow[i], mcolumn[j]) - grid[i][j]
        return res


def test_max_increase_keeping_skyline():
    s = Solution()
    assert 35 == s.maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4],
         [2, 4, 5, 7],
         [9, 2, 6, 3],
         [0, 3, 1, 0]])
