class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i + 1
        return -1


def test_is_prefix_of_word():
    s = Solution()
    assert 4 == s.isPrefixOfWord("i love eating burger", "burg")
    assert 2 == s.isPrefixOfWord("this problem is an easy problem", "pro")
    assert -1 == s.isPrefixOfWord("i am tired", "you")
    assert 4 == s.isPrefixOfWord("i use triple pillow", "pill")
    assert -1 == s.isPrefixOfWord("hello from the other side", "they")
