class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        m = {}
        for v in s:
            m[v] = m.get(v, 0) + 1
        for x in range(0, len(s)):
            if m[s[x]] == 1:
                i = x
                break
        return i


def test_first_uniq_char():
    s = Solution()
    assert 0 == s.firstUniqChar("leetcode")
    assert 2 == s.firstUniqChar("loveleetcode")
