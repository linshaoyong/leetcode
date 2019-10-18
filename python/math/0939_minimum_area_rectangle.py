class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """


def test_min_area_rect():
    s = Solution()
    assert 4 == s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
    assert 2 == s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]])
