class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp = {0}
        for stone in stones:
            dp = {stone + x for x in dp} | {abs(stone - x) for x in dp}
        return min(dp)


def test_last_stone_weight_ii():
    s = Solution()
    assert 1 == s.lastStoneWeightII([2, 7, 4, 1, 8, 1])
    assert 5 == s.lastStoneWeightII([31, 26, 33, 21, 40])
