class Solution(object):

    R1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
              'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'])
    R2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'])
    R3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm',
              'Z', 'X', 'C', 'V', 'B', 'N', 'M'])

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            first = word[0]
            one_row = True
            r = self.R1
            if first in self.R2:
                r = self.R2
            if first in self.R3:
                r = self.R3
            for w in word[1:]:
                if w not in r:
                    one_row = False
                    break
            if one_row:
                result.append(word)
        return result


def test_find_words():
    s = Solution()
    assert ["Alaska", "Dad"] == s.findWords(
        ["Hello", "Alaska", "Dad", "Peace"])
