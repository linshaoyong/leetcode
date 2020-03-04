class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                res += 4 * grid[i][j] + 2
                if j > 0:
                    res -= min(grid[i][j], grid[i][j - 1]) * 2
                if i > 0:
                    res -= min(grid[i][j], grid[i - 1][j]) * 2
        return res


def test_surface_area():
    s = Solution()
    assert 10 == s.surfaceArea([[2]])
    assert 34 == s.surfaceArea([[1, 2], [3, 4]])
    assert 16 == s.surfaceArea([[1, 0], [0, 2]])
    assert 32 == s.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert 46 == s.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]])
