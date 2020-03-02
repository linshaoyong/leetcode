class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        snums = sorted(nums)
        prev = snums[0]
        m = {snums[0]: 0}
        for i in range(1, len(snums)):
            if snums[i] == prev:
                continue
            m[snums[i]] = i
            prev = snums[i]
        return [m[n] for n in nums]


def test_smaller_numbers_than_current():
    s = Solution()
    assert [4, 0, 1, 1, 3] == s.smallerNumbersThanCurrent([8, 1, 2, 2, 3])
    assert [2, 1, 0, 3] == s.smallerNumbersThanCurrent([6, 5, 4, 8])
    assert [0, 0, 0, 0] == s.smallerNumbersThanCurrent([7, 7, 7, 7])
