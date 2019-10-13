class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return self.captures(board, i, j)

    def captures(self, board, i, j):
        res = 0
        for x in range(i - 1, -1, -1):
            if board[x][j] == 'B':
                break
            if board[x][j] == 'p':
                res += 1
                break

        for x in range(i + 1, 8):
            if board[x][j] == 'B':
                break
            if board[x][j] == 'p':
                res += 1
                break

        for x in range(j - 1, -1, -1):
            if board[i][x] == 'B':
                break
            if board[i][x] == 'p':
                res += 1
                break

        for x in range(j + 1, 8):
            if board[i][x] == 'B':
                break
            if board[i][x] == 'p':
                res += 1
                break

        return res


def test_num_rook_captures():
    s = Solution()
    assert 3 == s.numRookCaptures([
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]])

    assert 0 == s.numRookCaptures([
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "B", "R", "B", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]])

    assert 3 == s.numRookCaptures([
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        ["p", "p", ".", "R", ".", "p", "B", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]])
