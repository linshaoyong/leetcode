class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = []
        dp.append((costs[0], days[0],))
        dp.append((costs[1], days[0] + 6,))
        dp.append((costs[2], days[0] + 29,))

        for day in days[1:]:
            mincost = None
            remain = []
            for pp in dp:
                if pp[1] >= day:
                    remain.append(pp)
                else:
                    mincost = min(mincost, pp[0]) if mincost else pp[0]
            if mincost:
                remain.append((mincost + costs[0], day,))
                remain.append((mincost + costs[1], day + 6,))
                remain.append((mincost + costs[2], day + 29,))
            dp = remain

        dp.sort()
        return dp[0][0]


def test_mincost_tickets():
    s = Solution()
    assert 11 == s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
    assert 17 == s.mincostTickets(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15])
    assert 50 == s.mincostTickets(
        [1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 16, 17, 19, 21, 24, 26, 27, 28, 29],
        [3, 14, 50])
