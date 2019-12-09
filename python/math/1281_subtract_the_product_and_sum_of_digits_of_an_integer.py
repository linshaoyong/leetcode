class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p, s = 1, 0
        while n:
            a = n % 10
            p *= a
            s += a
            n = n // 10
        return p - s


def test_subtract_product_and_sum():
    s = Solution()
    assert 15 == s.subtractProductAndSum(234)
    assert 21 == s.subtractProductAndSum(4421)
