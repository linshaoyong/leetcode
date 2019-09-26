class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = {}
        acc, res = 0, 0
        for i in range(len(nums)):
            acc += nums[i]
            if acc - k in presum:
                res += presum[acc - k]
            if acc == k:
                res += 1
            presum[acc] = presum.get(acc, 0) + 1
        return res


def test_subarray_sum():
    assert 2 == Solution().subarraySum([1, 1, 1], 2)
