class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            c = min(a, b) + cost[i]
            a, b = b, c

        return min(a, b)


def test_min_cost_climbing_stairs():
    s = Solution()
    assert 8 == s.minCostClimbingStairs([10, 8])
    assert 15 == s.minCostClimbingStairs([10, 15, 20])
    assert 6 == s.minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
