class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = [["" for _ in range(3)] for _ in range(3)]
        for i in range(len(moves)):
            if i % 2 == 0:
                grid[moves[i][0]][moves[i][1]] = "A"
            else:
                grid[moves[i][0]][moves[i][1]] = "B"

        for i in range(3):
            winner = self._winner(*grid[i])
            if winner:
                return winner

        for j in range(3):
            winner = self._winner(grid[0][j], grid[1][j], grid[2][j])
            if winner:
                return winner

        winner = self._winner(grid[0][0], grid[1][1], grid[2][2])
        if winner:
            return winner

        winner = self._winner(grid[0][2], grid[1][1], grid[2][0])
        if winner:
            return winner

        return "Draw" if len(moves) == 9 else "Pending"

    def _winner(self, *moves):
        if all([m == "A" for m in moves]):
            return "A"
        if all([m == "B" for m in moves]):
            return "B"


def test_winnter():
    s = Solution()
    assert "B" == s._winner(*["B", "B", "B"])


def test_tictactoe():
    s = Solution()
    assert "A" == s.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]])
    assert "B" == s.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]])
    assert "Draw" == s.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [
                                 1, 2], [2, 1], [0, 1], [0, 2], [2, 2]])
    assert "Pending" == s.tictactoe([[0, 0], [1, 1]])
    assert "B" == s.tictactoe([[2, 2], [0, 2], [1, 0], [0, 1], [2, 0], [0, 0]])
