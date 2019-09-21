class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sn = sorted(nums)
        return [sn[i] for i in range(len(sn) - 1) if sn[i] == sn[i + 1]]


def test_find_duplicates():
    assert [2, 3] == Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
