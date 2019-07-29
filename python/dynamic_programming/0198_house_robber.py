class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0

        if length == 1:
            return nums[0]

        dp = [nums[0]]
        dp.append(max(nums[0], nums[1]))

        for i in range(2, length):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        return dp[-1]


def test_rob():
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
