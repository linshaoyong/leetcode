class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        t = 0
        for i in range(len(points) - 1):
            t += self._time(points[i], points[i + 1])
        return t

    def _time(self, pa, pb):
        t1 = abs(pb[0] - pa[0])
        t2 = abs(pb[1] - pa[1])
        return min(t1, t2) + abs(t2 - t1)


def test_min_time_to_visit_all_points():
    s = Solution()
    assert 7 == s.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]])
    assert 5 == s.minTimeToVisitAllPoints([[3, 2], [-2, 2]])
