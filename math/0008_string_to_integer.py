class Solution(object):
    def myAtoi(self, _str):
        """
        :type str: str
        :rtype: int
        """
        valid = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        signs = set(['-', '+'])
        ns = []
        ss = _str.strip()
        if len(ss) == 0:
            return 0
        for v in ss:
            if v in valid:
                ns.append(v)
                continue
            if v in signs and not len(ns):
                ns.append(v)
                continue
            break

        if not ns or (len(ns) == 1 and ns[0] in signs):
            return 0
        r = int(''.join(ns))
        if r < -2147483648:
            return -2147483648
        if r > 2147483647:
            return 2147483647
        return r


def test_my_a_to_i():
    s = Solution()
    assert 0 == s.myAtoi("0-1")
    assert 0 == s.myAtoi("+-2")
    assert 1 == s.myAtoi("+1")
    assert 0 == s.myAtoi("")
    assert 0 == s.myAtoi("-")
    assert 42 == s.myAtoi("42")
    assert -42 == s.myAtoi("   -42")
    assert 4193 == s.myAtoi("4193 with words")
    assert 0 == s.myAtoi("words and 987")
    assert -2147483648 == s.myAtoi("-91283472332")
