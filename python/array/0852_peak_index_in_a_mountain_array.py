class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(0, len(A)):
            if A[i] > A[i + 1]:
                return i


def test_peak_index_in_mountain_array():
    assert 1 == Solution().peakIndexInMountainArray([0, 1, 0])
    assert 1 == Solution().peakIndexInMountainArray([0, 2, 1, 0])
