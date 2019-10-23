class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return True


def test_check_possibility():
    s = Solution()
    assert s.checkPossibility([1])
    assert s.checkPossibility([4, 2, 3])
    assert s.checkPossibility([4, 2, 1]) is False
    assert s.checkPossibility([3, 4, 2, 3]) is False
    assert s.checkPossibility([1, 5, 4, 6, 7, 10, 8, 9]) is False
    assert s.checkPossibility([2, 3, 3, 2, 4])
    assert s.checkPossibility([-1, 4, 2, 3])
