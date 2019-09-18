class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


def test_search():
    s = Solution()
    assert 4 == s.search([4, 5, 6, 7, 0, 1, 2], 0)
    assert -1 == s.search([4, 5, 6, 7, 0, 1, 2], 3)
