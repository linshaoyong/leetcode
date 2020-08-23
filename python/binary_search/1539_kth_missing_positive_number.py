class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """


def test_find_kth_positive():
    s = Solution()

    assert 9 == s.findKthPositive([2, 3, 4, 7, 11], 5)
    assert 6 == s.findKthPositive([1, 2, 3, 4], 2)
    assert 1 == s.findKthPositive([2], 1)
    assert 2 == s.findKthPositive([1, 3], 1)
