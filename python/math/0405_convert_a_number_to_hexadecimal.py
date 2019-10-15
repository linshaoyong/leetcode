class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            num = num + 2**32
        hexs = ['0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        res = ''
        while num:
            res = hexs[num % 16] + res
            num = num // 16
        return res


def test_to_hex():
    s = Solution()
    assert '1a' == s.toHex(26)
    assert 'ffffffff' == s.toHex(-1)
