class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        k = len(needle)
        if k == 0:
            return 0
        for i in range(0, n):
            if n - i < k:
                return -1
            for j in range(0, k):
                if haystack[i + j] != needle[j]:
                    break
                if j == k - 1:
                    return i
        return -1


def test_str_str():
    s = Solution()
    assert 0 == s.strStr("", "")
    assert 0 == s.strStr("a", "")
    assert -1 == s.strStr("", "a")
    assert 2 == s.strStr("hello", "ll")
    assert -1 == s.strStr("aaaaa", "bba")
    assert 0 == s.strStr("mississippi", "mississippi")
