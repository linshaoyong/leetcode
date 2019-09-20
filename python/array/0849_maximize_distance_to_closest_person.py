class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """


def test_max_dist_to_closest():
    s = Solution()
    assert 2 == s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
    assert 3 == s.maxDistToClosest([1, 0, 0, 0])
