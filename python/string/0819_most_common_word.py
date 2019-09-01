import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        sb = set(banned)
        h = {}
        for word in re.findall(r'\w+', paragraph):
            w = word.lower()
            h[w] = h.get(w, 0) + 1

        for k, _ in sorted(h.items(), key=lambda kv: kv[1], reverse=True):
            if k not in sb:
                return k


def test_most_common_word():
    assert "ball" == Solution().mostCommonWord(
        "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])

    assert "b" == Solution().mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])
