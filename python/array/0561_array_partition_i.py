class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        sn = sorted(nums)
        for i in range(0, len(nums), 2):
            r += sn[i]
        return r


def test_array_pair_sum():
    s = Solution()
    assert 4 == s.arrayPairSum([1, 4, 3, 2])
