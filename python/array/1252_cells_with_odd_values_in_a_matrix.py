class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for i in range(m)] for j in range(n)]

        for indice in indices:
            r, c = indice[0], indice[1]
            for i in range(m):
                matrix[r][i] += 1
            for i in range(n):
                matrix[i][c] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 == 1:
                    res += 1
        return res


def test_odd_cells():
    s = Solution()
    assert 6 == s.oddCells(2, 3, [[0, 1], [1, 1]])
    assert 0 == s.oddCells(2, 2, [[1, 1], [0, 0]])
