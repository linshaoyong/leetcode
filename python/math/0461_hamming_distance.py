class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


def test_hamming_distance():
    assert Solution().hammingDistance(1, 4) == 2
