class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        ns = stones[:-2]
        ns.append(stones[-1] - stones[-2])
        return self.lastStoneWeightII(ns)


def test_last_stone_weight_ii():
    s = Solution()
    assert 1 == s.lastStoneWeightII([2, 7, 4, 1, 8, 1])
    assert 5 == s.lastStoneWeightII([31, 26, 33, 21, 40])
