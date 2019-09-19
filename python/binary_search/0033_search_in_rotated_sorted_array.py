class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] > target:
                if nums[mid] > nums[left] and nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] and nums[right] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return left if nums[left] == target else -1


def test_search():
    s = Solution()
    assert -1 == s.search([], 5)
    assert 4 == s.search([4, 5, 6, 7, 0, 1, 2], 0)
    assert -1 == s.search([4, 5, 6, 7, 0, 1, 2], 3)
    assert 1 == s.search([5, 1, 2, 3, 4], 1)
    assert 1 == s.search([4, 5, 6, 7, 0, 1, 2], 5)
    assert 1 == s.search([8, 9, 2, 3, 4], 9)
    assert 4 == s.search([4, 5, 6, 7, 8, 1, 2, 3], 8)
