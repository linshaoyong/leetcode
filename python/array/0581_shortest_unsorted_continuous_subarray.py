class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        sn = sorted(nums)
        for i in range(0, len(nums)):
            if nums[i] != sn[i]:
                break
            res -= 1

        if res == 0:
            return 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sn[i]:
                break
            res -= 1
        return res


def test_find_unsorted_subarray():
    assert 5 == Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
    assert 0 == Solution().findUnsortedSubarray([1, 2, 3, 4])
