class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3 or A[1] <= A[0] or A[-2] <= A[-1]:
            return False
        asc = True
        for i in range(1, len(A) - 1):
            if A[i] == A[i - 1]:
                return False
            if asc:
                if A[i] < A[i - 1]:
                    asc = False
                continue
            if A[i] > A[i - 1]:
                return False
        return True


def test_valid_mountain_array():
    s = Solution()
    assert s.validMountainArray([2, 1]) is False
    assert s.validMountainArray([3, 5, 5]) is False
    assert s.validMountainArray([0, 3, 2, 1])
