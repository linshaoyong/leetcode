class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """


def test_stone_game():
    s = Solution()
    assert s.stoneGame([5, 3, 4, 5])
    assert s.stoneGame([3, 2, 10, 4])
    assert s.stoneGame([3, 7, 2, 3])
    assert s.stoneGame([6, 9, 4, 3, 9, 8])
