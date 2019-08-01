class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sorted_nums = sorted(nums)
        for x in range(0, length, 3):
            if x == length - 1:
                return sorted_nums[x]
            if sorted_nums[x] != sorted_nums[x + 1]:
                return sorted_nums[x]
        return sorted_nums[0]


def test_single_number():
    s = Solution()
    assert 3 == s.singleNumber([2, 2, 3, 2])
    assert 99 == s.singleNumber([0, 1, 0, 1, 0, 1, 99])
