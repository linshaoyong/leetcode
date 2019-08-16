class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        v = 0
        first = True
        start_i = 0
        for i, c in enumerate(bin(N)[2:]):
            if c == '1':
                if first:
                    start_i = i
                    first = False
                else:
                    v = max(v, i - start_i)
                    start_i = i
        return v


def test_binary_gap():
    s = Solution()
    assert 2 == s.binaryGap(22)
    assert 2 == s.binaryGap(5)
    assert 1 == s.binaryGap(6)
    assert 0 == s.binaryGap(8)
    assert 2 == s.binaryGap(13)
