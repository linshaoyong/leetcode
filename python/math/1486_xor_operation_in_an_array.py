class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res


def test_xor_operation():
    s = Solution()
    assert 8 == s.xorOperation(5, 0)
    assert 8 == s.xorOperation(4, 3)
    assert 7 == s.xorOperation(1, 7)
    assert 2 == s.xorOperation(10, 5)
