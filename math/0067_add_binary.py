class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2))[2:])


def test_add_binary():
    s = Solution()
    assert "100" == s.addBinary("11", "1")
    assert "10101" == s.addBinary("1010", "1011")
