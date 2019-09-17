class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        res = -1
        return res


def test_repeated_string_match():
    s = Solution()
    assert 3 == s.repeatedStringMatch("abcd", "cdabcdab")
    assert -1 == s.repeatedStringMatch("leet", "code")
