class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        min_i, min_j = ops[0][0], ops[0][1]
        for i, j in ops:
            min_i = min(min_i, i)
            min_j = min(min_j, j)
        return min_i * min_j


def test_max_count():
    s = Solution()
    assert 9 == s.maxCount(3, 3, [])
    assert 4 == s.maxCount(3, 3, [[2, 2], [3, 3]])
