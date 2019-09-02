class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """


def test_gcd_of_strings():
    s = Solution()
    assert "ABC" == s.gcdOfStrings("ABCABC", "ABC")
    assert "AB" == s.gcdOfStrings("ABABAB", "ABAB")
    assert "" == s.gcdOfStrings("LEET", "CODE")
