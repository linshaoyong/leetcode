class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = {}
        for a in arr:
            m[a] = m.get(a, 0) + 1
        res = 0
        for k, v in m.items():
            if k == v:
                res = max(res, k)
        return res if res else -1


def test_find_lucky():
    s = Solution()
    assert 2 == s.findLucky([2, 2, 3, 4])
    assert 3 == s.findLucky([1, 2, 2, 3, 3, 3])
    assert -1 == s.findLucky([2, 2, 2, 3, 3])
    assert -1 == s.findLucky([5])
    assert 7 == s.findLucky([7, 7, 7, 7, 7, 7, 7])
