class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


def test_four_sum():
    s = Solution()

    res = s.fourSum([1, 0, -1, 0, -2, 2], 0)
    assert 3 == len(res)
    assert [-1, 0, 0, 1] in res
    assert [-2, -1, 1, 2] in res
    assert [-2, 0, 0, 2] in res
