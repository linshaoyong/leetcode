class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = 0
        while True:
            ones, transforms = 0, []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        ones += 1
                        if i > 0 and grid[i - 1][j] == 2:
                            transforms.append((i, j,))
                            continue
                        if i < len(grid) - 1 and grid[i + 1][j] == 2:
                            transforms.append((i, j,))
                            continue
                        if j > 0 and grid[i][j - 1] == 2:
                            transforms.append((i, j,))
                            continue
                        if j < len(grid[i]) - 1 and grid[i][j + 1] == 2:
                            transforms.append((i, j,))
                            continue
            if not transforms:
                return -1 if ones > 0 else 0
            if ones == len(transforms):
                r += 1
                return r
            for x, y in transforms:
                grid[x][y] = 2
            r += 1


def test_oranges_rotting():
    s = Solution()
    assert 4 == s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    assert -1 == s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    assert 0 == s.orangesRotting([[0, 2]])
    assert -1 == s.orangesRotting([[0, 1]])
