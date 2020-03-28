class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0
        for a1 in arr1:
            dv = True
            for a2 in arr2:
                if abs(a1 - a2) <= d:
                    dv = False
                    break
            if dv:
                res += 1
        return res


def test_find_the_distance_value():
    s = Solution()
    assert 2 == s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2)
    assert 2 == s.findTheDistanceValue(
        [1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3)
    assert 1 == s.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6)
