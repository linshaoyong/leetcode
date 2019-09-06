class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0


def test_divisor_game():
    assert Solution().divisorGame(2)
    assert Solution().divisorGame(3) is False
