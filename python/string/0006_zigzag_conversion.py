class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """


def test_convert():
    s = Solution()
    assert "PAHNAPLSIIGYIR" == s.convert("PAYPALISHIRING", 3)
    assert "PINALSIGYAHRPI" == s.convert("PAYPALISHIRING", 4)
