class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)


def test_array_strings_are_equal():
    s = Solution()
    assert s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
    assert s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False
    assert s.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])
