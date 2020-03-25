class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res


def test_create_target_array():
    s = Solution()
    assert [0, 4, 1, 3, 2] == s.createTargetArray(
        [0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
    assert [0, 1, 2, 3, 4] == s.createTargetArray(
        [1, 2, 3, 4, 0], [0, 1, 2, 3, 0])
    assert [1] == s.createTargetArray([1], [0])
