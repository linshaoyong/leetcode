class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """


def test_character_replacement():
    s = Solution()
    assert 4 == s.characterReplacement("ABAB", 2)
    assert 4 == s.characterReplacement("AABABBA", 1)
    assert 4 == s.characterReplacement("ABBB", 2)
    assert 2 == s.characterReplacement("ABAA", 0)
    assert 3 == s.characterReplacement("BAAA", 0)
    assert 0 == s.characterReplacement("", 0)
