class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for j in range(0, len(A[0])):
            row = [A[i][j] for i in range(0, len(A))]
            res.append(row)
        return res


def test_transpose():
    assert [[1, 4, 7], [2, 5, 8], [3, 6, 9]] == Solution(
    ).transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    assert [[1, 4], [2, 5], [3, 6]] == Solution(
    ).transpose([[1, 2, 3], [4, 5, 6]])
