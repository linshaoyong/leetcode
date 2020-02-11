class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return True
        target_i = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] >= target_i - i:
                target_i = i
        return target_i == 0


def test_can_jump():
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False
