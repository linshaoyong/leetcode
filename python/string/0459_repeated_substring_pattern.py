class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, 0
        for i in range(1, len(s)):
            if s[i] != s[0]:
                end += 1
            else:
                if self.repeated(s, end - start + 1):
                    return True
                else:
                    end += 1
        return False

    def repeated(self, s, k):
        if len(s) % k != 0:
            return False
        for i in range(k, len(s), k):
            if s[i:i + k] != s[i - k:i]:
                return False
        return True


def test_repeated_substring_pattern():
    s = Solution()
    assert s.repeatedSubstringPattern("abab")
    assert s.repeatedSubstringPattern("aba") is False
    assert s.repeatedSubstringPattern("abcabcabcabc")
