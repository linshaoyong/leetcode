class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


def test_remove_duplicates():
    s = Solution()

    nums = [1]
    assert 1 == s.removeDuplicates(nums)
    assert [1] == nums

    nums = [1, 2]
    assert 2 == s.removeDuplicates(nums)
    assert [1, 2] == nums

    nums = [1, 1, 1]
    assert 1 == s.removeDuplicates(nums)
    assert [1, 1, 1] == nums

    nums = [1, 1, 2]
    assert 2 == s.removeDuplicates(nums)
    assert [1, 2, 2] == nums

    nums = [1, 1, 1, 2]
    assert 2 == s.removeDuplicates(nums)
    assert [1, 2, 1, 2] == nums

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert 5 == s.removeDuplicates(nums)
    assert [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] == nums

    nums = [-1, 0, 0, 0, 0, 0, 3, 3]
    assert 3 == s.removeDuplicates(nums)
    assert [-1, 0, 3, 0, 0, 0, 3, 3] == nums
