class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        min_a = A[0]
        max_a = A[0]
        for v in A:
            min_a = min(v, min_a)
            max_a = max(v, max_a)
        r = max_a - K - (min_a + K)
        return r if r > 0 else 0


def test_smallest_range_i():
    s = Solution()

    assert 0 == s.smallestRangeI([1], 0)
    assert 6 == s.smallestRangeI([0, 10], 2)
    assert 0 == s.smallestRangeI([1, 3, 6], 3)
