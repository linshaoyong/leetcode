class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        row, down = 0, True
        for i in range(len(s)):
            res[row].append(s[i])
            if down:
                row += 1
                if row == numRows - 1:
                    down = False
            else:
                row -= 1
                if row == 0:
                    down = True
        return ''.join([''.join(a) for a in res])


def test_convert():
    s = Solution()
    assert "PAHNAPLSIIGYIR" == s.convert("PAYPALISHIRING", 3)
    assert "PINALSIGYAHRPI" == s.convert("PAYPALISHIRING", 4)
    assert "AB" == s.convert("AB", 1)
