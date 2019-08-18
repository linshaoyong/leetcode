class Solution(object):

    M = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
         "e": ".", "f": "..-.", "g": "--.", "h": "....",
         "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
         "m": "--", "n": "-.", "o": "---", "p": ".--.",
         "q": "--.-", "r": ".-.", "s": "...", "t": "-",
         "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
         "y": "-.--", "z": "--.."}

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = set()
        for w in words:
            s.add(''.join([self.M.get(c) for c in w]))
        return len(s)


def test_():
    s = Solution()
    assert 2 == s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
