class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, columns = len(mat), len(mat[0])
        i, j = rows - 1, 1
        while i > 0:
            i -= 1
            self.diagonalize(mat, i, 0)

        while j < columns:
            self.diagonalize(mat, 0, j)
            j += 1
        return mat

    def diagonalize(self, mat, start_x, start_y):
        rows, columns = len(mat), len(mat[0])
        x, y, values = start_x, start_y, []
        while x < rows and y < columns:
            values.append(mat[x][y])
            x += 1
            y += 1
        x, y = start_x, start_y
        values.sort()
        for v in values:
            mat[x][y] = v
            x += 1
            y += 1


def test_diagonal_sort():
    s = Solution()
    assert [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]] == s.diagonalSort(
        [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
