class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        start = end = 0
        for i in range(0, len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)
            length = max(len1, len2)
            if length > (end - start):
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


def test_longest_palindrome():
    r = Solution().longestPalindrome("babad")
    assert r == "bab" or r == "aba"

    r = Solution().longestPalindrome("cbbd")
    assert r == "bb"
