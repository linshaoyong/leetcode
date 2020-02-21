class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stations = []
        for n, s, e in trips:
            stations.append((s, n))
            stations.append((e, -n))
        c = 0
        for _, v in sorted(stations):
            c += v
            if c > capacity:
                return False
        return True


def test_car_pooling():
    s = Solution()
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 4) is False
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 5)
    assert s.carPooling([[2, 1, 5], [3, 5, 7]], 3)
    assert s.carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11)
