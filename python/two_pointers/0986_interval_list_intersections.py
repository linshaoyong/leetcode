class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j, res = 0, 0, []
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            if a[0] > b[1]:
                j += 1
                continue
            if b[0] > a[1]:
                i += 1
                continue
            res.append([max(a[0], b[0]), min(a[1], b[1])])
            if a[1] <= b[1]:
                i += 1
            else:
                j += 1
        return res


def test_interval_intersection():
    assert [[1, 2], [5, 5], [8, 10], [15, 23],
            [24, 24], [25, 25]] == Solution().intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]])
