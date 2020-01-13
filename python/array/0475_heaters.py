class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        sorted_houses = sorted(houses)
        sorted_heaters = sorted(heaters)
        res = 0
        for house in sorted_houses:
            left, right = 0, len(sorted_heaters) - 1
            mid = (left + right) // 2
            while mid > left and mid < right:
                if house == sorted_heaters[mid]:
                    break
                if house > sorted_heaters[mid]:
                    left = mid
                    mid = (left + right) // 2
                else:
                    right = mid
                    mid = (left + right) // 2
            v = min(abs(sorted_heaters[mid] - house),
                    abs(sorted_heaters[right] - house))
            res = max(res, v)
        return res


def test_find_radius():
    s = Solution()
    assert 1 == s.findRadius([1, 2, 3], [2])
    assert 1 == s.findRadius([1, 2, 3, 4], [1, 4])
    assert 3 == s.findRadius([1, 5], [2])
    assert 0 == s.findRadius([1], [1, 2, 3, 4])
    assert 161834419 == s.findRadius([282475249, 622650073, 984943658,
                                      144108930, 470211272, 101027544,
                                      457850878, 458777923],
                                     [823564440, 115438165, 784484492,
                                      74243042, 114807987, 137522503,
                                      441282327, 16531729, 823378840,
                                      143542612])
