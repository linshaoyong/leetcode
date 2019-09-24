class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        sa = [v for v in s]
        i, j = 0, len(s) - 1
        while i < j:
            if sa[i] in vowels:
                while j > i:
                    if sa[j] in vowels:
                        sa[i], sa[j] = sa[j], sa[i]
                        j -= 1
                        break
                    j -= 1

            i += 1
        return ''.join(sa)


def test_reverse_vowels():
    s = Solution()
    assert "holle" == s.reverseVowels("hello")
    assert "leotcede" == s.reverseVowels("leetcode")
    assert "Aa" == s.reverseVowels("aA")
