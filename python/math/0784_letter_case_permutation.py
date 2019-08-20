class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        count = 0
        for s in S:
            if s.isalpha():
                count += 1
        ss = S.lower()
        result = []
        for i in range(0, pow(2, count)):
            b = bin(i)[2:]
            r = []
            j = 1
            for s in ss:
                if s.isalpha():
                    if j <= len(b) and b[-j] == '1':
                        r.append(s.upper())
                        j += 1
                        continue
                    j += 1
                r.append(s)
            result.append(''.join(r))
        return result


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
