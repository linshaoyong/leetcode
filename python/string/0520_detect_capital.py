class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if self.is_upper(word[0]):
            if len(word) < 3:
                return True
            b = self.is_upper(word[1])
            for c in word[2:]:
                if self.is_upper(c) != b:
                    return False
        else:
            for c in word[1:]:
                if self.is_upper(c):
                    return False
        return True

    def is_upper(self, c):
        return c >= 'A' and c <= 'Z'


def test_detect_capital_use():
    s = Solution()
    assert s.detectCapitalUse("USA")
    assert s.detectCapitalUse("ggg")
    assert s.detectCapitalUse("FlaG") is False
