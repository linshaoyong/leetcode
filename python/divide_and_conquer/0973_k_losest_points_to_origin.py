class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:K]


def test_k_closest():
    s = Solution()
    assert [[-2, 2]] == s.kClosest([[1, 3], [-2, 2]], 1)
    res = s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert 2 == len(res)
    assert [3, 3] in res
    assert [-2, 4] in res
