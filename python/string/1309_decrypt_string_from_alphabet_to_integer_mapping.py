class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        n = len(s) - 1
        while n >= 0:
            if s[n] == '#':
                res.append(s[n - 2:n])
                n -= 3
            else:
                res.append(s[n])
                n -= 1
        res.reverse()
        return "".join([chr(int(c) + 96)for c in res])


def test_freq_alphabets():
    s = Solution()
    assert "jkab" == s.freqAlphabets("10#11#12")
    assert "acz" == s.freqAlphabets("1326#")
    assert "y" == s.freqAlphabets("25#")
    assert "abcdefghijklmnopqrstuvwxyz" == s.freqAlphabets(
        "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
