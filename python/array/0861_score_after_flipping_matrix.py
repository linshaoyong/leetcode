class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    A[i][j] = A[i][j] ^ 1
        res = 0
        for j in range(len(A[0])):
            zeros, ones = 0, 0
            for i in range(len(A)):
                if A[i][j] == 0:
                    zeros += 1
                else:
                    ones += 1
            res += max(zeros, ones) * pow(2, len(A[0]) - j - 1)
        return res


def test_matrix_score():
    s = Solution()
    assert 39 == s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
