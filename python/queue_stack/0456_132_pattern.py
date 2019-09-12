class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return False


def test_find132pattern():
    s = Solution()
    assert s.find132pattern([1, 2, 3, 4]) is False
    assert s.find132pattern([3, 1, 4, 2])
    assert s.find132pattern([-1, 3, 2, 0])
