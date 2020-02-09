class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            dm = {}
            for q in points:
                dx = p[0] - q[0]
                dy = p[1] - q[1]
                ds = dx * dx + dy * dy
                dm[ds] = 1 + dm.get(ds, 0)
            for k in dm:
                res += dm[k] * (dm[k] - 1)
        return res


def test_number_of_boomerangs():
    s = Solution()
    assert 2 == s.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
