class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        p1, p2, p3 = points[0], points[1], points[2]
        if p2[0] != p1[0]:
            a = (p2[1] - p1[1]) / float(p2[0] - p1[0])
            b = p1[1] - a * p1[0]
            return p3[1] != (a * p3[0] + b)
        else:
            return p3[0] != p2[0] and p1[1] != p2[1]


def test_is_boomerang():
    s = Solution()
    assert s.isBoomerang([[1, 1], [2, 3], [3, 2]])
    assert s.isBoomerang([[1, 1], [2, 2], [3, 3]]) is False
    assert s.isBoomerang([[1, 1], [1, 2], [1, 3]]) is False
    assert s.isBoomerang([[0, 0], [1, 1], [1, 1]]) is False
    assert s.isBoomerang([[0, 0], [2, 1], [2, 1]]) is False
    assert s.isBoomerang([[0, 1], [0, 1], [2, 1]]) is False
