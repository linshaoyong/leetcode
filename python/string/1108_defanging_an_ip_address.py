class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ss = []
        for s in address:
            if s == '.':
                ss.append('[.]')
            else:
                ss.append(s)
        return ''.join(ss)


def test_defang_ip_addr():
    s = Solution()
    assert "1[.]1[.]1[.]1" == s.defangIPaddr("1.1.1.1")
    assert "255[.]100[.]50[.]0" == s.defangIPaddr("255.100.50.0")
