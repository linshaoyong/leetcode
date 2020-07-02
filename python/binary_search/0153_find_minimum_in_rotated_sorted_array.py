class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, prev = nums[0], nums[0]
        for n in nums:
            if n < prev:
                return n
            prev = n
        return res


def test_find_min():
    s = Solution()
    assert 1 == s.findMin([3, 4, 5, 1, 2])
    assert 0 == s.findMin([4, 5, 6, 7, 0, 1, 2])
