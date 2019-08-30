class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """


def test_cal_points():
    s = Solution()
    assert 30 == s.calPoints(["5", "2", "C", "D", "+"])
    assert 27 == s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
