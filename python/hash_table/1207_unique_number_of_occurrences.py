class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        m = {}
        for a in arr:
            m[a] = m.get(a, 0) + 1
        return len(m) == len(set(m.values()))


def test_unique_occurrences():
    s = Solution()
    assert s.uniqueOccurrences([1, 2, 2, 1, 1, 3])
    assert s.uniqueOccurrences([1, 2]) is False
    assert s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
