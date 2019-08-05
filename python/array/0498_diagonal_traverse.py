class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        r, c, m, n = 0, 0, len(matrix), len(matrix[0])
        arr = []
        for _ in range(m * n):
            arr.append(matrix[r][c])
            if (r + c) % 2 == 0:  # moving up
                if (c == n - 1):
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:                 # moving down
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return arr


def test_find_diagonal_order():
    s = Solution()
    assert [1, 2, 4, 7, 5, 3, 6, 8, 9] == s.findDiagonalOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
