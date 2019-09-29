class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        max_avg = s / k
        for i in range(k, len(nums)):
            s = s - nums[i - k] + nums[i]
            avg = s / k
            max_avg = max(max_avg, avg)
        return max_avg


def test_find_max_average():
    s = Solution()
    assert 12.75 == s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
