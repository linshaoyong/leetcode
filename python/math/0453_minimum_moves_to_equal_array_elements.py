class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxv, minv = max(nums), min(nums)
        if len(nums) < 3 or maxv == minv:
            return maxv - minv


def test_min_moves():
    s = Solution()
    assert 3 == s.minMoves([1, 2, 3])
    assert 0 == s.minMoves([1, 1, 1])
    assert 2147483646 == s.minMoves([1, 1, 2147483647])
