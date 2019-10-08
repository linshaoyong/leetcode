class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = 1
        ar = A * n
        while len(ar) < len(B):
            n += 1
            ar = A * n
        if B not in ar:
            n += 1
            ar = A * n
        if B in ar:
            return n
        return -1


def test_repeated_string_match():
    s = Solution()
    assert 3 == s.repeatedStringMatch("abcd", "cdabcdab")
    assert -1 == s.repeatedStringMatch("leet", "code")
