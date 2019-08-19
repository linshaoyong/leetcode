class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ws = {}
        for w in A.split():
            ws[w] = ws.get(w, 0) + 1
        for w in B.split():
            ws[w] = ws.get(w, 0) + 1
        return [k for k, v in ws.items() if v == 1]


def test_uncommon_from_sentences():
    s = Solution()
    r = s.uncommonFromSentences("this apple is sweet", "this apple is sour")
    assert 2 == len(r)
    assert "sweet" in r
    assert "sour" in r
