class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        if s % k != 0:
            return False


def test_can_partition_k_subsets():
    s = Solution()
    assert s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
