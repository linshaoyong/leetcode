class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return []

        res = ['']
        for i in range(0, len(S)):
            if S[i].isalpha():
                vvv = []
                for r in res:
                    vvv.append(r + S[i].lower())
                    vvv.append(r + S[i].upper())
                res = vvv
            else:
                res = [r + S[i] for r in res]
        return res


def test_letter_case_permutation():
    s = Solution()
    r = s.letterCasePermutation("a1b2")
    assert 4 == len(r)
    assert "a1b2" in r
    assert "a1B2" in r
    assert "A1b2" in r
    assert "A1B2" in r

    r = s.letterCasePermutation("3z4")
    assert 2 == len(r)
    assert "3z4" in r
    assert "3Z4" in r

    assert ["12345"] == s.letterCasePermutation("12345")
