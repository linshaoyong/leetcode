class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if len(word) == len(pattern):
                d1, d2 = {}, {}
                match = True
                for i in range(len(word)):
                    if word[i] in d1:
                        if d1[word[i]] != pattern[i]:
                            match = False
                            break
                    else:
                        d1[word[i]] = pattern[i]

                    if pattern[i] in d2:
                        if d2[pattern[i]] != word[i]:
                            match = False
                            break
                    else:
                        d2[pattern[i]] = word[i]
                if match:
                    res.append(word)
        return res


def test_find_and_replace_pattern():
    s = Solution()
    assert ["mee", "aqq"] == s.findAndReplacePattern(
        ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
