class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = {0: 0, 1: 0, 2: 0}
        for n in nums:
            m[n] = m.get(n) + 1

        for i in range(m[0]):
            nums[i] = 0

        for i in range(m[0], m[0] + m[1]):
            nums[i] = 1

        for i in range(m[0] + m[1], len(nums)):
            nums[i] = 2
        return nums


def test_sort_colors():
    r = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(r)
    assert [0, 0, 1, 1, 2, 2] == r
