class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        r = '-' if num < 0 else ''
        s = []
        n = abs(num)
        while n > 0:
            s.append(str(n % 7))
            n = n // 7
        return r + ''.join(s[::-1])


def test_convert_to_base7():
    s = Solution()
    assert "0" == s.convertToBase7(0)
    assert "202" == s.convertToBase7(100)
    assert "-10" == s.convertToBase7(-7)
