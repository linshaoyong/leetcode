class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n, m = len(grid), len(grid[0])
        for _ in range(k):
            for j in range(m - 1, 0, -1):
                for i in range(n):
                    grid[i][j], grid[i][j - 1] = grid[i][j - 1], grid[i][j]
            for i in range(n - 1, 0, -1):
                grid[i][0], grid[i - 1][0] = grid[i - 1][0], grid[i][0]
        return grid


def test_shift_grid():
    s = Solution()
    assert [[9, 1, 2],
            [3, 4, 5],
            [6, 7, 8]] == s.shiftGrid(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]], 1)

    assert [[12, 0, 21, 13],
            [3, 8, 1, 9],
            [19, 7, 2, 5],
            [4, 6, 11, 10]] == s.shiftGrid(
        [[3, 8, 1, 9],
         [19, 7, 2, 5],
         [4, 6, 11, 10],
         [12, 0, 21, 13]], 4)

    assert [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]] == s.shiftGrid(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]], 9)
