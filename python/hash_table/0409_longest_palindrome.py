class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        for c in s:
            h[c] = h.get(c, 0) + 1
        r = 0
        has_odd = False
        for k, v in h.items():
            if v % 2 == 0:
                r += v
            else:
                r += v - 1
                has_odd = True
        if has_odd:
            r += 1
        return r


def test_longest_palindrome():
    assert 7 == Solution().longestPalindrome("abccccdd")
    assert 3 == Solution().longestPalindrome("ccc")
