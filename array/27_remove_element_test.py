class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        i = 0
        for j in range(0, n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


def test_remove_element():
    s = Solution()
    nums = [4, 5]
    assert 1 == s.removeElement(nums, 4)
    assert [5] == nums[:1]

    nums = [3, 2, 2, 3]
    assert 2 == s.removeElement(nums, 3)
    assert [2, 2] == nums[:2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert 5 == s.removeElement(nums, 2)
    assert [0, 1, 3, 0, 4] == nums[:5]
