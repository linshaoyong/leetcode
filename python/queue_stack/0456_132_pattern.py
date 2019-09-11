class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1, -1, -1):
            v = nums[i]
            right = False
            for j in range(i, -1, -1):
                if not right and nums[j] > v:
                    right = True
                if right and nums[j] < v:
                    return True
        return False


def test_find132pattern():
    s = Solution()
    assert s.find132pattern([1, 2, 3, 4]) is False
    assert s.find132pattern([3, 1, 4, 2])
    assert s.find132pattern([-1, 3, 2, 0])
