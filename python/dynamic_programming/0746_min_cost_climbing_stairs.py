class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """


def test_min_cost_climbing_stairs():
    s = Solution()
    assert 15 == s.minCostClimbingStairs([10, 15, 20])
    assert 6 == s.minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
