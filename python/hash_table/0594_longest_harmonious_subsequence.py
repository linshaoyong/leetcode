class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        r = 0
        for k, v in h.items():
            if k - 1 in h:
                r = max(r, v + h[k - 1])
            if k + 1 in h:
                r = max(r, v + h[k + 1])
        return r


def test_find_lhs():
    assert 0 == Solution().findLHS([1, 1, 1, 1])
    assert 5 == Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7])
