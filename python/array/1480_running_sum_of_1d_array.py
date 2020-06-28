class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, s = [0] * len(nums), 0
        for i in range(len(nums)):
            res[i] = nums[i] + s
            s = res[i]
        return res


def test_running_sum():
    s = Solution()
    assert [1, 3, 6, 10] == s.runningSum([1, 2, 3, 4])
    assert [1, 2, 3, 4, 5] == s.runningSum([1, 1, 1, 1, 1])
    assert [3, 4, 6, 16, 17] == s.runningSum([3, 1, 2, 10, 1])
