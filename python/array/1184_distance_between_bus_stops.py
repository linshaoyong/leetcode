class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        st = min(start, destination)
        et = max(start, destination)
        s, t = 0, 0
        for i in range(len(distance)):
            s += distance[i]
            if i >= st and i < et:
                t += distance[i]
        return min(t, s - t)


def test_distance_between_bus_stops():
    s = Solution()
    assert 1 == s.distanceBetweenBusStops([1, 2, 3, 4], 0, 1)
    assert 3 == s.distanceBetweenBusStops([1, 2, 3, 4], 0, 2)
    assert 4 == s.distanceBetweenBusStops([1, 2, 3, 4], 0, 3)
    assert 17 == s.distanceBetweenBusStops(
        [7, 10, 1, 12, 11, 14, 5, 0], 7, 2)
