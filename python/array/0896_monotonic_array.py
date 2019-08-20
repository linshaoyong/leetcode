class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return True
        order = A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] > A[i - 1]:
                if order < 0:
                    return False
                order = 1
            if A[i] < A[i - 1]:
                if order > 0:
                    return False
                order = -1
        return True


def test_is_monotonic():
    s = Solution()

    assert s.isMonotonic([1, 2, 2, 3])
    assert s.isMonotonic([6, 5, 4, 4])
    assert s.isMonotonic([1, 3, 2]) is False
    assert s.isMonotonic([1, 2, 4, 5])
    assert s.isMonotonic([1, 1, 1])
    assert s.isMonotonic([1, 1, 2])
