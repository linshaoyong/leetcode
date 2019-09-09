class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        ds = set(dict)
        res = []
        for word in sentence.split():
            successor = False
            for i in range(len(word)):
                if word[:i] in ds:
                    res.append(word[:i])
                    successor = True
                    break
            if not successor:
                res.append(word)
        return ' '.join(res)


def test_replace_words():
    assert "the cat was rat by the bat" == Solution().replaceWords(
        ["cat", "bat", "rat"], "the cattle was rattled by the battery")

    assert "a a a a a a a a bbb baba a" == Solution().replaceWords(
        ["a", "aa", "aaa", "aaaa"],
        "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")
