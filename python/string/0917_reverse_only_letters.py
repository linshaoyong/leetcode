class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        symbols = {}
        for i in range(0, len(S)):
            if not S[i].isalpha():
                symbols[i] = S[i]
        res = []
        for i in range(len(S) - 1, -1, -1):
            while len(res) in symbols:
                res.append(symbols[len(res)])
            if S[i].isalpha():
                res.append(S[i])
                while len(res) in symbols:
                    res.append(symbols[len(res)])
        return ''.join(res)


def test_reverse_only_letters():
    s = Solution()
    assert "dc-ba" == s.reverseOnlyLetters("ab-cd")
    assert "j-Ih-gfE-dCba" == s.reverseOnlyLetters("a-bC-dEf-ghIj")
    assert "Qedo1ct-eeLg=ntse-T!" == s.reverseOnlyLetters(
        "Test1ng-Leet=code-Q!")
    assert "j<*zz" == s.reverseOnlyLetters("z<*zj")
    assert ";1VDy" == s.reverseOnlyLetters(";1yDV")
