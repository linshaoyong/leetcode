class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        v = 1
        x = num
        while x > 0:
            v = v * 2
            x = x // 2
            print(v, x)
        return v - 1 - num


def test_find_complement():
    s = Solution()
    assert 2 == s.findComplement(5)
    assert 0 == s.findComplement(1)
