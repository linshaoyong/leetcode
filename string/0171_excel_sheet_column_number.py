class Solution(object):

    D = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
         'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
         'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
         'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    def titleToNumber(self, s):
        r = 0
        length = len(s)
        for i, val in enumerate(s):
            r += self.D[val] * (26**(length - i - 1))
        return r


def test_title_to_number():
    s = Solution()
    assert 1 == s.titleToNumber("A")
    assert 28 == s.titleToNumber("AB")
    assert 701 == s.titleToNumber("ZY")
