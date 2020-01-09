class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """


def test_find_radius():
    s = Solution()
    assert 1 == s.findRadius([1, 2, 3], [2])
    assert 1 == s.findRadius([1, 2, 3, 4], [1, 4])
    assert 3 == s.findRadius([1, 5], [2])
