class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


def test_is_palindrome():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    assert s.isPalindrome("race a car") is False
    assert s.isPalindrome("") is True
    assert s.isPalindrome("   ") is True
