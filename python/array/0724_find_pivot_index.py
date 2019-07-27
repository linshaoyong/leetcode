class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        sp = 0
        for i in range(0, len(nums)):
            if (s - nums[i]) % 2 == 0 and sp == (s - nums[i]) // 2:
                return i
            sp = sp + nums[i]
        return -1


def test_pivot_index():
    s = Solution()
    assert 3 == s.pivotIndex([1, 7, 3, 6, 5, 6])
    assert -1 == s.pivotIndex([1, 2, 3])
