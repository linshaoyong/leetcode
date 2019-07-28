class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


def test_can_win_nim():
    s = Solution()
    assert s.canWinNim(4) is False
