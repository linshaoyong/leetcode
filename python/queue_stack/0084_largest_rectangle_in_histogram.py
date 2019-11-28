class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """


def test_largest_rectangle_area():
    s = Solution()
    assert 10 == s.largestRectangleArea([2, 1, 5, 2, 6, 3])
