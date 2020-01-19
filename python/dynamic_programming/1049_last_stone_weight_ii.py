class Solution(object):
    def lastStoneWeightII(self, stones):
        dp = {0}
        sumv = sum(stones)
        for stone in stones:
            dp |= {stone + d for d in dp}
        return min(abs(sumv - d - d) for d in dp)


def test_last_stone_weight_ii():
    s = Solution()
    assert 1 == s.lastStoneWeightII([2, 7, 4, 1, 8, 1])
    assert 5 == s.lastStoneWeightII([31, 26, 33, 21, 40])
    assert 97 == s.lastStoneWeightII([1, 2, 100])
