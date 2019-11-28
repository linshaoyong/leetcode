class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res


def test_max_sliding_window():
    assert [] == Solution().maxSlidingWindow([], 0)
    assert [3, 3, 5, 5, 6, 7] == Solution().maxSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3)
