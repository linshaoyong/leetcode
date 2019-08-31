class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lps = {}
        for p in licensePlate:
            if p.isalpha():
                pl = p.lower()
                lps[pl] = lps.get(pl, 0) + 1

        find = ""
        for word in words:
            matched = True
            for k, v in lps.items():
                if word.count(k) < v:
                    matched = False
                    break
            if matched and (not find or len(find) > len(word)):
                find = word
        return find


def test_shortest_completing_word():
    assert "steps" == Solution().shortestCompletingWord(
        "1s3 PSt", ["step", "steps", "stripe", "stepple"])
    assert "pest" == Solution().shortestCompletingWord(
        "1s3 456", ["looks", "pest", "stew", "show"])
