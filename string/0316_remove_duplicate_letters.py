class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """


def test_remove_duplicate_letters():
    s = Solution()
    assert "abc" == s.removeDuplicateLetters("bcabc")
    assert "acdb" == s.removeDuplicateLetters("cbacdcbc")
