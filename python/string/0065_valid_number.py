class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1

        is_numeric = False
        while i < n and s[i].isnumeric():
            i += 1
            is_numeric = True

        if i < n and s[i] == '.':
            i += 1
            while i < n and s[i].isnumeric():
                i += 1
                is_numeric = True

        if is_numeric and i < n and s[i] == 'e':
            i += 1
            is_numeric = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < n and s[i].isnumeric():
                i += 1
                is_numeric = True

        while i < n and s[i] == ' ':
            i += 1
        return is_numeric and i == n


def test_is_number():
    s = Solution()
    assert s.isNumber("0")
    assert s.isNumber(" 0.1 ")
    assert s.isNumber("abc") is False
    assert s.isNumber("1 a") is False
    assert s.isNumber("2e10")
    assert s.isNumber(" -90e3   ")
    assert s.isNumber(" 1e") is False
    assert s.isNumber("e3") is False
    assert s.isNumber(" 6e-1")
    assert s.isNumber(" 99e2.5 ") is False
    assert s.isNumber("53.5e93")
    assert s.isNumber(" --6 ") is False
    assert s.isNumber("-+3") is False
    assert s.isNumber("95a54e53") is False
