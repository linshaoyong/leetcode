class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] != 5:
                    continue
                a1, a2, a3 = grid[i - 1][j - 1], grid[i - 1][j], \
                    grid[i - 1][j + 1]
                a4, a5, a6 = grid[i][j - 1], grid[i][j], grid[i][j + 1]
                a7, a8, a9 = grid[i + 1][j - 1], grid[i + 1][j], \
                    grid[i + 1][j + 1]

                if set([a1, a2, a3, a4, a5, a6, a7, a8, a9]) != \
                        set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
                    continue

                if a1 + a2 + a3 != 15:
                    continue
                if a4 + a5 + a6 != 15:
                    continue
                if a7 + a8 + a9 != 15:
                    continue
                if a1 + a4 + a7 != 15:
                    continue
                if a2 + a5 + a8 != 15:
                    continue
                if a3 + a6 + a9 != 15:
                    continue
                if a1 + a5 + a9 != 15:
                    continue
                if a3 + a5 + a7 != 15:
                    continue
                res += 1
        return res


def test_num_magic_squares_inside():
    s = Solution()
    #assert 1 == s.numMagicSquaresInside([[4, 3, 8, 4],
    #                                     [9, 5, 1, 9],
    #                                     [2, 7, 6, 2]])

    assert 1 == s.numMagicSquaresInside([[3, 10, 2, 3, 4],
                                         [4, 5, 6, 8, 1],
                                         [8, 8, 1, 6, 8],
                                         [1, 3, 5, 7, 1],
                                         [9, 4, 9, 2, 9]])
