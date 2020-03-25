class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle = abs(6 * minutes - (30 * hour + minutes / 2))
        return min(angle, 360 - angle)


def test_angle_clock():
    s = Solution()
    assert 165 == s.angleClock(12, 30)
    assert 75 == s.angleClock(3, 30)
    assert 7.5 == s.angleClock(3, 15)
    assert 155 == s.angleClock(4, 50)
    assert 0 == s.angleClock(12, 0)
