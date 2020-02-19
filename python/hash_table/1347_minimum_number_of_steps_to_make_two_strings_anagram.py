class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = {}
        for a in s:
            m[a] = m.get(a, 0) + 1
        for a in t:
            m[a] = m.get(a, 0) - 1
        return sum([v for v in m.values() if v > 0])


def test_min_steps():
    s = Solution()
    assert 1 == s.minSteps("bab", "aba")
    assert 5 == s.minSteps("leetcode", "practice")
    assert 0 == s.minSteps("anagram", "mangaar")
    assert 0 == s.minSteps("xxyyzz", "xxyyzz")
    assert 4 == s.minSteps("friend", "family")
