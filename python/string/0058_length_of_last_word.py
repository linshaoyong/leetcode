class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = i
        for v in s:
            if v == ' ':
                if i != 0:
                    j = i
                    i = 0
            else:
                i += 1
        return j if i == 0 else i


def test_length_of_last_word():
    s = Solution()
    assert 5 == s.lengthOfLastWord("Hello World")
    assert 5 == s.lengthOfLastWord("Hello World     ")
    assert 5 == s.lengthOfLastWord("    Hello World     ")
    assert 1 == s.lengthOfLastWord("a ")
