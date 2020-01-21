class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        for num in nums:
            if num <= target:
                dp[num] = 1
        for i in range(target + 1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i - num]
        return dp[-1]


def test_combination_sum():
    s = Solution()
    assert 7 == s.combinationSum4([1, 2, 3], 4)
    assert 39882198 == s.combinationSum4([4, 2, 1], 32)
