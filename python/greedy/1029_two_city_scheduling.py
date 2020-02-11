class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        scs = sorted(costs, key=lambda cost: cost[0] - cost[1])
        mid = len(scs) // 2
        r = 0
        for i in range(mid):
            r += scs[i][0]
        for i in range(mid, len(scs)):
            r += scs[i][1]
        return r


def test_two_city_sched_cost():
    s = Solution()
    assert 110 == s.twoCitySchedCost(
        [[10, 20], [30, 200], [400, 50], [30, 20]])
