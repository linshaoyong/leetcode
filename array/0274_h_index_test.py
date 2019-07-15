class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        sc = sorted(citations)
        v = 0
        for i in range(n - 1, -1, -1):
            if sc[i] >= n - i:
                if i == 0:
                    return n - i
                if sc[i - 1] <= n - i:
                    return n - i
        return v


def test_h_index():
    s = Solution()
    assert 3 == s.hIndex([3, 0, 6, 1, 5])
    assert 3 == s.hIndex([4, 0, 6, 1, 5])
    assert 4 == s.hIndex([4, 0, 6, 4, 5])
    assert 0 == s.hIndex([])
    assert 0 == s.hIndex([0])
    assert 1 == s.hIndex([1])
    assert 1 == s.hIndex([100])
    assert 1 == s.hIndex([1, 2])
    assert 1 == s.hIndex([1, 1])
