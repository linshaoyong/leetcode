class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_mins = [0] * len(matrix)
        col_maxs = matrix[0]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == 0:
                    row_mins[i] = matrix[i][j]
                else:
                    row_mins[i] = min(row_mins[i], matrix[i][j])
                col_maxs[j] = max(col_maxs[j], matrix[i][j])
        return list(set(row_mins) & set(col_maxs))


def test_luckyNumbers():
    s = Solution()
    assert [15] == s.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]])
    assert [12] == s.luckyNumbers(
        [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]])
    assert [7] == s.luckyNumbers([[7, 8], [1, 2]])
