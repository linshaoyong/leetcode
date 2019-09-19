class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                right = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid + 1
                left = mid + 1
        if nums[left] < target:
            return left + 1
        return left


def test_search_insert():
    s = Solution()
    assert 0 == s.searchInsert([1], 0)
    assert 0 == s.searchInsert([0], 0)
    assert 1 == s.searchInsert([1], 2)
    assert 1 == s.searchInsert([1, 3], 2)
    assert 2 == s.searchInsert([1, 3, 5, 6], 5)
    assert 1 == s.searchInsert([1, 3, 5, 6], 2)
    assert 4 == s.searchInsert([1, 3, 5, 6], 7)
    assert 0 == s.searchInsert([1, 3, 5, 6], 0)
