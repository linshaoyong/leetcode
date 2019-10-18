class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        res = []
        queens = {(i, j) for i, j in queens}
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        for (i, j) in directions:
            for k in range(1, 8):
                x, y = king[0] + i * k, king[1] + j * k
                if (x, y) in queens:
                    res.append([x, y])
                    break
        return res


def test_queens_attack_the_king():
    s = Solution()
    r = s.queensAttacktheKing(
        [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], [0, 0])
    assert 3 == len(r)
    assert [0, 1] in r
    assert [1, 0] in r
    assert [3, 3] in r
