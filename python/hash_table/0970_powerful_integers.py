class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        xx = self.sqrt(x, bound)
        yy = self.sqrt(y, bound)
        res = set()
        for i in range(0, xx):
            a = pow(x, i)
            for j in range(0, yy):
                b = pow(y, j)
                s = a + b
                if s > bound:
                    break
                res.add(s)
        return list(res)

    def sqrt(self, x, bound):
        if x == 1:
            return 1
        v = 0
        while bound > 0:
            bound = bound // x
            v += 1
        return v


def test_powerful_integers():
    r = Solution().powerfulIntegers(2, 3, 10)
    assert 7 == len(r)
    assert 2 in r
    assert 3 in r
    assert 4 in r
    assert 5 in r
    assert 7 in r
    assert 9 in r
    assert 10 in r

    assert [2] == Solution().powerfulIntegers(2, 3, 2)

    r = Solution().powerfulIntegers(3, 5, 15)
    assert 6 == len(r)
    assert 2 in r
    assert 4 in r
    assert 6 in r
    assert 8 in r
    assert 10 in r
    assert 14 in r
