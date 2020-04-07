class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        groups = {}
        for i in range(1, n + 1):
            ds = self.digit_sum(i)
            groups[ds] = groups.get(ds, 0) + 1
        vs = sorted(groups.values(), reverse=True)
        res, m = 1, vs[0]
        for v in vs[1:]:
            if v != m:
                break
            res += 1
        return res

    def digit_sum(self, i):
        res = 0
        while i > 0:
            res += i % 10
            i = i // 10
        return res


def test_count_largest_group():
    s = Solution()
    assert 4 == s.countLargestGroup(13)
    assert 2 == s.countLargestGroup(2)
    assert 6 == s.countLargestGroup(15)
    assert 5 == s.countLargestGroup(24)
