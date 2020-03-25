class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        powers = {1: 0, 2: 1}
        for x in range(lo, hi + 1, 1):
            if x in powers:
                continue
            tmp = []
            while x != 1:
                tmp.append(x)
                if self.fill_power(tmp, powers, x):
                    break
                x = x // 2 if x % 2 == 0 else 3 * x + 1

        res = []
        for x in range(lo, hi + 1, 1):
            res.append((powers.get(x), x))
        return sorted(res)[k - 1][1]

    def fill_power(self, arr, powers, found):
        if arr[-1] in powers:
            i = 0
            for v in arr[::-1]:
                powers[v] = powers[found] + i
                i += 1
            return True
        return False


def test_get_kth():
    s = Solution()
    assert 13 == s.getKth(lo=12, hi=15, k=2)
    assert 1 == s.getKth(lo=1, hi=1, k=1)
    assert 7 == s.getKth(lo=7, hi=11, k=4)
    assert 13 == s.getKth(lo=10, hi=20, k=5)
    assert 570 == s.getKth(lo=1, hi=1000, k=777)
