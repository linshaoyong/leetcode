class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for v in nums:
            if i < 2 or v > nums[i - 2]:
                nums[i] = v
                i += 1
        return i


def test_remove_duplicates():
    s = Solution()

    nums = [1, 1, 1]
    assert 2 == s.removeDuplicates(nums)
    assert [1, 1] == nums[:2]

    nums = [1, 2, 2]
    assert 3 == s.removeDuplicates(nums)
    assert [1, 2, 2] == nums[:3]

    nums = [1, 1, 2, 2]
    assert 4 == s.removeDuplicates(nums)
    assert [1, 1, 2, 2] == nums[:4]

    nums = [1, 1, 1, 1, 1, 2]
    assert 3 == s.removeDuplicates(nums)
    assert [1, 1, 2] == nums[:3]

    nums = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    assert 9 == s.removeDuplicates(nums)
    assert [0, 0, 1, 1, 2, 2, 3, 3, 4] == nums[:9]

    nums = [0, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4]
    assert 7 == s.removeDuplicates(nums)
    assert [0, 1, 2, 2, 3, 4, 4] == nums[:7]

    nums = [1, 1, 1, 2, 2, 2, 3, 3]
    assert 6 == s.removeDuplicates(nums)
    assert [1, 1, 2, 2, 3, 3] == nums[:6]

    nums = [1, 2]
    assert 2 == s.removeDuplicates(nums)
    assert [1, 2] == nums[:2]

    nums = [1, 1, 1, 2, 2, 3]
    assert 5 == s.removeDuplicates(nums)
    assert [1, 1, 2, 2, 3] == nums[:5]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert 7 == s.removeDuplicates(nums)
    assert [0, 0, 1, 1, 2, 3, 3] == nums[:7]
