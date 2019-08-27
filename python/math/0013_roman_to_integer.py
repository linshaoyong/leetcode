class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]


def test_roman_to_int():
    s = Solution()
    assert 3 == s.romanToInt("III")
    assert 4 == s.romanToInt("IV")
    assert 9 == s.romanToInt("IX")
    assert 58 == s.romanToInt("LVIII")
    assert 1994 == s.romanToInt("MCMXCIV")
