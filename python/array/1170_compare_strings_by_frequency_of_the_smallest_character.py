class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        fws = sorted([self.frequency(word) for word in words], reverse=True)
        res = []
        for query in queries:
            n = 0
            fq = self.frequency(query)
            for fw in fws:
                if fq < fw:
                    n += 1
                else:
                    break
            res.append(n)
        return res

    def frequency(self, word):
        if not word:
            return 0
        sw = sorted(word)
        smallest = sw[0]
        n = 1
        for w in sw[1:]:
            if w == smallest:
                n += 1
        return n


def test_num_smaller_by_frequency():
    assert [1] == Solution().numSmallerByFrequency(["cbd"], ["zaaaz"])
    assert [1, 2] == Solution().numSmallerByFrequency(
        ["bbb", "cc"], ["a", "aa", "aaa", "aaaa"])
