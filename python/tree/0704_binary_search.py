class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, low, hight):
        mid = low + (hight - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            if mid + 1 > hight:
                return -1
            return self.binary_search(nums, target, mid + 1, hight)
        if low > mid - 1:
            return -1
        return self.binary_search(nums, target, low, mid - 1)


def test_search():
    s = Solution()
    assert 4 == s.search([-1, 0, 3, 5, 9, 12], 9)
    assert -1 == s.search([-1, 0, 3, 5, 9, 12], 2)
    assert 0 == s.search([5], 5)
    assert 1 == s.search([2, 5], 5)
