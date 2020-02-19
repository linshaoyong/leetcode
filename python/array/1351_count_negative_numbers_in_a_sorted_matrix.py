class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        rows, columns = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] < 0:
                    res += columns - j
                    break
        return res


def test_count_negatives():
    s = Solution()
    assert 8 == s.countNegatives(
        [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
    assert 0 == s.countNegatives([[3, 2], [1, 0]])
    assert 3 == s.countNegatives([[1, -1], [-1, -1]])
    assert 1 == s.countNegatives([[-1]])
