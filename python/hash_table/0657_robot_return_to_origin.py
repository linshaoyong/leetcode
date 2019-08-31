class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {}
        for move in moves:
            d[move] = d.get(move, 0) + 1
        return d.get('U', 0) == d.get('D', 0) and \
            d.get('L', 0) == d.get('R', 0)


def test_judge_circle():
    assert Solution().judgeCircle("UD")
    assert Solution().judgeCircle("LL") is False
    assert Solution().judgeCircle("RLUURDDDLU")
