class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return [list(i) for i in res]


def test_three_sum():
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    assert len(result) == 2
    assert [-1, 0, 1] in result
    assert [-1, -1, 2] in result
