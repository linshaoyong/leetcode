import operator


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1

        sorted_x = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        return [kk for kk, _ in sorted_x[:k]]


def test_top_k_frequent():
    s = Solution()
    assert [1, 2] == s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert [1] == s.topKFrequent([1], 1)
