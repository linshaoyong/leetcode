class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """


def test_push_dominoes():
    s = Solution()
    assert "LL.RR.LLRRLL.." == s.pushDominoes(".L.R...LR..L..")
    assert "RR.L" == s.pushDominoes("RR.L")
