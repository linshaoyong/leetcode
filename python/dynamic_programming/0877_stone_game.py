class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        memo = [[-1] * n for _ in range(n)]
        return self.max_stones(piles, 0, n - 1, memo) > (sum(piles) // 2)

    def max_stones(self, piles, st, en, memo):
        if st > en:
            return 0
        if en - st <= 1:
            return max(piles[st], piles[en])
        if memo[st][en] != -1:
            return memo[st][en]
        v = max(self.max_stones(piles, st + 1, en, memo) + piles[st],
                self.max_stones(piles, st, en - 1, memo) + piles[en])
        memo[st][en] = v
        return v


def test_stone_game():
    s = Solution()
    assert s.stoneGame([5, 3, 4, 5])
    assert s.stoneGame([3, 2, 10, 4])
    assert s.stoneGame([3, 7, 2, 3])
    assert s.stoneGame([6, 9, 4, 3, 9, 8])
