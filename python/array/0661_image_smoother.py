class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        r = [[0] * len(row) for row in M]

        for i in range(len(M)):
            row = M[i]
            v, n = 0, 0
            for j in range(len(row)):
                v, n = M[i][j], 1
                points = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                          (i, j - 1), (i, j + 1),
                          (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
                for x, y in points:
                    if x >= 0 and x < len(M) and y >= 0 and y < len(row):
                        v += M[x][y]
                        n += 1
                r[i][j] = v // n
        return r


def test_image_smoother():
    s = Solution()

    assert [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]] == s.imageSmoother([[1, 1, 1],
                                           [1, 0, 1],
                                           [1, 1, 1]])
