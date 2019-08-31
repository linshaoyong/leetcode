class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, len(s)):
            if s[i] == s[len(s) - 1 - i]:
                continue
            if self.is_palindrome(s[i + 1:len(s) - i]):
                return True
            if self.is_palindrome(s[i:len(s) - 1 - i]):
                return True
            return False
        return True

    def is_palindrome(self, s):
        print(s)
        for i in range(0, len(s) // 2 + 1):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


def test_valid_palindrome():
    assert Solution().validPalindrome("aba")
    assert Solution().validPalindrome("abc") is False
    assert Solution().validPalindrome("abca")
    assert Solution().validPalindrome("deeee")
