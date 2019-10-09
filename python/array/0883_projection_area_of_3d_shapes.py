class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a, b, c = 0, 0, 0
        for j in range(len(grid[0])):
            m = 0
            for i in range(len(grid)):
                if grid[i][j] > 0:
                    a += 1
                m = max(m, grid[i][j])
                if j == 0:
                    c += max(grid[i])
            b += m
        return a + b + c


def test_projection_area():
    s = Solution()
    assert 5 == s.projectionArea([[2]])
    assert 17 == s.projectionArea([[1, 2], [3, 4]])
    assert 8 == s.projectionArea([[1, 0], [0, 2]])
    assert 14 == s.projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert 21 == s.projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]])
