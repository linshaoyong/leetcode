class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.vowels = set(['a', 'e', 'i', 'o', 'u',
                           'A', 'E', 'I', 'O', 'U'])
        halve = len(s) // 2
        return self.count_vowel(s[:halve]) == self.count_vowel(s[halve:])

    def count_vowel(self, s):
        a = 0
        for c in s:
            if c in self.vowels:
                a += 1
        return a


def test_halves_are_alike():
    s = Solution()
    assert s.halvesAreAlike("book")
    assert s.halvesAreAlike("textbook") is False
    assert s.halvesAreAlike("MerryChristmas") is False
    assert s.halvesAreAlike("AbCdEfGh")
