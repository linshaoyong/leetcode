class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return False


def test_find_duplicate():
    s = Solution()
    assert 2 == s.findDuplicate([1, 3, 4, 2, 2])
    assert 3 == s.findDuplicate([3, 1, 3, 4, 2])
