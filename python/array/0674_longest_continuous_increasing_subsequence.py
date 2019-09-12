class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        r, start = 0, 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                r = max(r, i - start)
                start = i
            prev = nums[i]
        return max(r, len(nums) - start)


def test_find_length_of_lcis():
    assert 0 == Solution().findLengthOfLCIS([])
    assert 3 == Solution().findLengthOfLCIS([1, 3, 5, 4, 7])
    assert 1 == Solution().findLengthOfLCIS([2, 2, 2, 2, 2])
    assert 5 == Solution().findLengthOfLCIS([1, 3, 5, 7, 9])
