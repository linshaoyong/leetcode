class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0

        result = 0
        for i in range(0, 32):
            result <<= 1
            if (n & 1) == 1:
                result += 1
            n >>= 1
        return result


def test_reverse_bits():
    s = Solution()
    assert 964176192 == s.reverseBits(43261596)
    assert 3221225471 == s.reverseBits(4294967293)
