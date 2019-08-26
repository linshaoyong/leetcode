class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        r = 0
        cs = {}
        for c in chars:
            cs[c] = cs.get(c, 0) + 1
        for word in words:
            m = {}
            formed = True
            for w in word:
                m[w] = m.get(w, 0) + 1
                if m[w] > cs.get(w, 0):
                    formed = False
                    break
            if formed:
                r += len(word)
        return r


def test_count_characters():
    s = Solution()
    assert 6 == s.countCharacters(["cat", "bt", "hat", "tree"], "atach")
    assert 10 == s.countCharacters(
        ["hello", "world", "leetcode"], "welldonehoneyr")
