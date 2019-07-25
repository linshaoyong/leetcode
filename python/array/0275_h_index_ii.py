class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        v = 0
        for i in range(n - 1, -1, -1):
            if citations[i] >= n - i:
                if i == 0:
                    return n - i
                if citations[i - 1] <= n - i:
                    return n - i
        return v


def test_h_index():
    s = Solution()
    assert 3 == s.hIndex([0, 1, 3, 5, 6])
