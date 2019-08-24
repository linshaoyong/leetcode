class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss = {}
        for c in s:
            ss[c] = ss.get(c, 0) + 1
        for c in t:
            if c not in ss:
                return c
            ss[c] = ss.get(c) - 1
            if ss[c] == 0:
                ss.pop(c)


def test_find_the_difference():
    s = Solution()
    assert "e" == s.findTheDifference("abcd", "abcde")
    assert "a" == s.findTheDifference("a", "aa")
    assert "a" == s.findTheDifference("ae", "aea")
