class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """


def test_repeated_substring_pattern():
    s = Solution()
    assert s.repeatedSubstringPattern("abab")
    assert s.repeatedSubstringPattern("aba") is False
    assert s.repeatedSubstringPattern("abcabcabcabc")
