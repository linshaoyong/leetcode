class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        sn = str(n)
        res = [sn[-3:]]
        for i in range(len(sn) - 4, -1, -3):
            res.append(".")
            res.append(sn[max(0, i - 2):i + 1])
        return "".join(res[::-1])


def test_thousand_separator():
    s = Solution()
    assert "987" == s.thousandSeparator(987)
    assert "1.234" == s.thousandSeparator(1234)
    assert "0" == s.thousandSeparator(0)
    assert "51.040" == s.thousandSeparator(51040)
    assert "123.456.789" == s.thousandSeparator(123456789)
