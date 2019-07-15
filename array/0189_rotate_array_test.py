class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, _nums, _start, _end):
        while _start < _end:
            _nums[_start], _nums[_end] = _nums[_end], _nums[_start]
            _start += 1
            _end -= 1


def test_rotate():
    s = Solution()

    nums = [1]
    s.rotate(nums, 0)
    assert [1] == nums

    nums = [1, 2]
    s.rotate(nums, 3)
    assert [2, 1] == nums

    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    assert [5, 6, 7, 1, 2, 3, 4] == nums

    nums = [-1, -100, 3, 99]
    s.rotate(nums, 2)
    assert [3, 99, -1, -100] == nums

    nums = [2147483647, -2147483648, 33, 219, 0]
    s.rotate(nums, 4)
    assert [-2147483648, 33, 219, 0, 2147483647] == nums

    nums = [1, 2, 3, 4, 5, 6]
    s.rotate(nums, 4)
    assert [3, 4, 5, 6, 1, 2] == nums

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
            15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    s.rotate(nums, 38)
    assert [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2,
            3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] == nums
