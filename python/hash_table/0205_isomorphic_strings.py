class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m1, m2 = {}, {}
        for i in range(0, len(s)):
            if s[i] in m1 and m1[s[i]] != t[i]:
                    return False
            if t[i] in m2 and m2[t[i]] != s[i]:
                    return False
            m1[s[i]] = t[i]
            m2[t[i]] = s[i]
        return True


def test_is_isomorphic():
    s = Solution()
    assert s.isIsomorphic("egg", "add") is True
    assert s.isIsomorphic("foo", "bar") is False
    assert s.isIsomorphic("paper", "title") is True
    assert s.isIsomorphic("ab", "aa") is False
