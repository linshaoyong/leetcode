class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m1, m2 = {}, {}
        ss = str.split()
        if len(pattern) != len(ss):
            return False
        for i in range(0, len(pattern)):
            if pattern[i] in m1 and m1[pattern[i]] != ss[i]:
                return False
            if ss[i] in m2 and m2[ss[i]] != pattern[i]:
                return False
            m1[pattern[i]] = ss[i]
            m2[ss[i]] = pattern[i]
        return True


def test_word_pattern():
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog") is True
    assert s.wordPattern("abba", "dog cat cat fish") is False
    assert s.wordPattern("aaaa", "dog cat cat dog") is False
    assert s.wordPattern("abba", "dog dog dog dog") is False
    assert s.wordPattern("abba", "dog dog dog dog") is False
