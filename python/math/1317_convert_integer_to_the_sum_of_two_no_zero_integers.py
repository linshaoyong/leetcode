class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n):
            if '0' not in f'{i}{n-i}':
                return [i, n - i]


def test_get_no_zero_integers():
    s = Solution()
    assert [1, 1] == s.getNoZeroIntegers(2)
    assert [1, 213] == s.getNoZeroIntegers(214)
    assert [58, 999] == s.getNoZeroIntegers(1057)
