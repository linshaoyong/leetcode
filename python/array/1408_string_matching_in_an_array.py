class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = set()
        for i in range(len(words)):
            wi = words[i]
            for j in range(i + 1, len(words)):
                wj = words[j]
                if wi in wj:
                    res.add(wi)
                if wj in wi:
                    res.add(wj)
        return list(res)


def test_string_matching():
    s = Solution()
    res = s.stringMatching(
        ["mass", "as", "hero", "superhero"])
    assert 2 == len(res)
    assert "as" in res
    assert "hero" in res

    res = s.stringMatching(["leetcode", "et", "code"])
    assert 2 == len(res)
    assert "et" in res
    assert "code" in res

    res = s.stringMatching(["leetcoder", "leetcode", "od", "hamlet", "am"])
    assert 3 == len(res)
    assert "leetcode" in res
    assert "od" in res
    assert "am" in res

    assert [] == s.stringMatching(["blue", "green", "bu"])
