class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        repeates = []
        for i in range(1, len(str1)):
            if str1[i] == str1[0]:
                if self.repeated(str1, str1[0:i]):
                    repeates.append(str1[0:i])
        repeates.append(str1)
        for rep in repeates[::-1]:
            if self.repeated(str2, rep):
                return rep
        return ""

    def repeated(self, s, sk):
        if len(s) % len(sk) != 0:
            return False
        for i in range(0, len(s), len(sk)):
            if s[i:i + len(sk)] != sk:
                return False
        return True


def test_gcd_of_strings():
    s = Solution()
    assert "ABC" == s.gcdOfStrings("ABCABC", "ABC")
    assert "AB" == s.gcdOfStrings("ABABAB", "ABAB")
    assert "" == s.gcdOfStrings("LEET", "CODE")
    assert "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" == s.gcdOfStrings(
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
