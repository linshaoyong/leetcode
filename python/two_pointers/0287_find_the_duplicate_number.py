class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 1, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            counter = 0
            for num in nums:
                if num <= mid:
                    counter += 1

            if counter > mid:
                end = mid
            else:
                start = mid + 1
        return start


def test_find_duplicate():
    s = Solution()
    assert 2 == s.findDuplicate([1, 3, 4, 2, 2])
    assert 3 == s.findDuplicate([3, 1, 3, 4, 2])
