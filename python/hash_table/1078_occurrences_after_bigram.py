class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        result = []
        words = text.split()
        for i, word in enumerate(words):
            if word == second:
                if i > 0 and words[i - 1] == first and i + 1 < len(words):
                    result.append(words[i + 1])
        return result


def test_find_ocurrences():
    s = Solution()
    assert ["girl", "student"] == s.findOcurrences(
        "alice is a good girl she is a good student", "a", "good")
    assert ["we", "rock"] == s.findOcurrences(
        "we will we will rock you", "we", "will")
