class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        m = {'1': '0', '0': '1'}
        return int('0b' + ''.join([m.get(i) for i in bin(N)[2:]]), 2)


def test_bitwise_complement():
    s = Solution()
    assert 2 == s.bitwiseComplement(5)
    assert 0 == s.bitwiseComplement(7)
    assert 5 == s.bitwiseComplement(10)
