class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n % 2 == 1:
            res.append(0)
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        return res


def test_sumZero():
    s = Solution()
    assert [0] == s.sumZero(1)
    assert [1, -1] == s.sumZero(2)
    assert [0, 1, -1] == s.sumZero(3)
    assert [1, -1, 2, -2] == s.sumZero(4)
    assert [0, 1, -1, 2, -2] == s.sumZero(5)
    assert [1, -1, 2, -2, 3, -3] == s.sumZero(6)
