class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return True


def test_is_scramble():
    s = Solution()
    assert s.isScramble("great", "rgeat") is True
    assert s.isScramble("abcde", "caebd") is False
