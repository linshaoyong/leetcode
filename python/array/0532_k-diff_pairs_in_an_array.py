class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        hnums = {}
        for n in nums:
            hnums[n] = hnums.get(n, 0) + 1

        v = 0
        for n, c in hnums.items():
            if k == 0:
                if c > 1:
                    v += 1
            else:
                if n - k in hnums:
                    v += 1
                if n + k in hnums:
                    v += 1
        return v if k == 0 else v // 2


def test_find_pairs():
    s = Solution()
    assert 2 == s.findPairs([3, 1, 4, 1, 5], 2)
    assert 4 == s.findPairs([1, 2, 3, 4, 5], 1)
    assert 1 == s.findPairs([1, 3, 1, 5, 4], 0)
    assert 1 == s.findPairs([1, 1, 1, 2, 1], 1)
    assert 1 == s.findPairs([1, 1, 1, 1, 1], 0)
    assert 1 == s.findPairs([1, 1, 1, 2, 2], 1)
    assert 0 == s.findPairs([1, 2, 3, 4, 5], -1)
