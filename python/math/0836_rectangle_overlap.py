class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return ((rec1[2] > rec2[0] and rec1[2] <= rec2[2]) or (
            rec2[2] > rec1[0] and rec2[2] <= rec1[2])) and (
            (rec1[3] > rec2[1] and rec1[3] <= rec2[3]) or (
                rec2[3] > rec1[1] and rec2[3] <= rec1[3]))


def test_is_rectangle_overlap():
    s = Solution()
    assert s.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])
    assert s.isRectangleOverlap([2, 17, 6, 20], [3, 8, 6, 20])
    assert s.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]) is False
