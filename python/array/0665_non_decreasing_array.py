class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True

        c, k = 0, 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                c += 1
                if c > 1:
                    return False
                k = i

        if c == 0:
            return True

        if k == 1 or k == len(nums) - 1:
            return True

        if nums[k] >= nums[k - 2] or nums[k + 1] >= nums[k - 1]:
            return True

        return False


def test_check_possibility():
    s = Solution()
    assert s.checkPossibility([1])
    assert s.checkPossibility([4, 2, 3])
    assert s.checkPossibility([4, 2, 1]) is False
    assert s.checkPossibility([3, 4, 2, 3]) is False
    assert s.checkPossibility([1, 5, 4, 6, 7, 10, 8, 9]) is False
    assert s.checkPossibility([2, 3, 3, 2, 4])
    assert s.checkPossibility([-1, 4, 2, 3])
    assert s.checkPossibility([1, 2, 3])
    assert s.checkPossibility([1, 3, 2])
