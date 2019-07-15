class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return 0


def test_h_index():
    s = Solution()
    assert 3 == s.hIndex([3, 0, 6, 1, 5])
    assert 0 == s.hIndex([])
    assert 0 == s.hIndex([0])
    assert 1 == s.hIndex([1])
    assert 1 == s.hIndex([100])
    assert 1 == s.hIndex([1, 2])
    assert 1 == s.hIndex([1, 1])
