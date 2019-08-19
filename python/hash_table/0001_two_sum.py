class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            d[target - nums[i]] = i


def test_two_sum():
    s = Solution()
    a = s.twoSum([2, 7, 11, 15], 13)
    assert a == [0, 2]

    a = s.twoSum([2, 7, 11, 15, 9, 6], 16)
    assert a == [1, 4]

    a = s.twoSum([3, 2, 4], 6)
    assert a == [1, 2]

    a = s.twoSum([-3, 4, 3, 90], 0)
    assert a == [0, 2]
