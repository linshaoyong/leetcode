class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        sws = set(words)
        ws = sorted(words, key=lambda x: len(x), reverse=True)
        find = ""
        length = 0
        for word in ws:
            if find and len(word) < length:
                break
            wanted = True
            for i in range(len(word) - 1, 0, -1):
                if not word[0:i] in sws:
                    wanted = False
                    break
            if wanted:
                if not find or word < find:
                    find = word
                    length = len(find)
        return find


def test_longest_word():
    assert "world" == Solution().longestWord(
        ["w", "wo", "wor", "worl", "world"])
    assert "apple" == Solution().longestWord(
        ["a", "banana", "app", "appl", "ap", "apply", "apple"])
    assert "breakfast" == Solution().longestWord(
        ["b", "br", "bre", "brea", "break", "breakf", "breakfa",
         "breakfas", "breakfast", "l", "lu", "lun", "lunc", "lunch",
         "d", "di", "din", "dinn", "dinne", "dinner"])
    assert "english" == Solution().longestWord(
        ["t", "ti", "tig", "tige", "tiger", "e", "en", "eng",
         "engl", "engli", "englis", "english", "h", "hi",
         "his", "hist", "histo", "histor", "history"])
