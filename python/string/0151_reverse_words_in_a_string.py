class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


def test_reverse_words():
    s = Solution()
    assert "blue is sky the" == s.reverseWords("the sky is blue")
    assert "world! hello" == s.reverseWords("  hello world!  ")
    assert "example good a" == s.reverseWords("a good   example")
