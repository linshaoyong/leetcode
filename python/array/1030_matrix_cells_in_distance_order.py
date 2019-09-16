class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        hm = {}
        for i in range(R):
            for j in range(C):
                distance = abs(i - r0) + abs(j - c0)
                v = hm.get(distance, [])
                v.append([i, j])
                hm[distance] = v
        res = []
        for k in sorted(hm):
            res.extend(hm[k])
        return res


def test_all_cells_distOrder():
    s = Solution()
    r = s.allCellsDistOrder(1, 2, 0, 0)
    assert 2 == len(r)
    assert [0, 0] in r
    assert [0, 1] in r

    r = s.allCellsDistOrder(2, 2, 0, 1)
    assert 4 == len(r)
    assert [0, 1] in r
    assert [0, 0] in r
    assert [1, 1] in r
    assert [1, 0] in r

    r = s.allCellsDistOrder(2, 3, 1, 2)
    assert 6 == len(r)
    assert [1, 2] in r
    assert [0, 2] in r
    assert [1, 1] in r
    assert [0, 1] in r
    assert [1, 0] in r
    assert [0, 0] in r
