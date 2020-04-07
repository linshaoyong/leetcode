class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] != nums[mid + 1]:
                high = mid
            else:
                low = mid + 2
        return nums[low]


def test_single_non_duplicate():
    s = Solution()
    assert 1 == s.singleNonDuplicate([1])
    assert 2 == s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    assert 10 == s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
    assert 2 == s.singleNonDuplicate([1, 1, 2, 3, 3])
