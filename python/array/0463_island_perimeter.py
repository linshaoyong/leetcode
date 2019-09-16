class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i == 0:
                        res += 1
                    if i == len(grid) - 1:
                        res += 1

                    if i > 0 and grid[i - 1][j] == 0:
                        res += 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 0:
                        res += 1

                    if j == 0:
                        res += 1
                    if j == len(grid[i]) - 1:
                        res += 1

                    if j > 0 and grid[i][j - 1] == 0:
                        res += 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 0:
                        res += 1
        return res


def test_island_perimeter():
    assert 16 == Solution().islandPerimeter([[0, 1, 0, 0],
                                             [1, 1, 1, 0],
                                             [0, 1, 0, 0],
                                             [1, 1, 0, 0]])

    assert 4 == Solution().islandPerimeter([[1]])
    assert 4 == Solution().islandPerimeter([[1, 0]])
