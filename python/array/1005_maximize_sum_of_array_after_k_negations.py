class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        k = K
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = -A[i]
                k -= 1
            else:
                break
            if k == 0:
                return sum(A)
        A.sort()
        A[0] = A[0] if k % 2 == 0 else -A[0]
        return sum(A)


def test_largest_sum_after_k_negations():
    s = Solution()
    assert 5 == s.largestSumAfterKNegations([4, 2, 3], 1)
    assert 6 == s.largestSumAfterKNegations([3, -1, 0, 2], 3)
    assert 13 == s.largestSumAfterKNegations([2, -3, -1, 5, -4], 2)
