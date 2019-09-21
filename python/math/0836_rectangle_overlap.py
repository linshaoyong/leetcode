class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """


def test_is_rectangle_overlap():
    s = Solution()
    assert s.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])
    assert s.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]) is False
