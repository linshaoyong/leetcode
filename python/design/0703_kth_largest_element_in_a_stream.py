class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """


def test_kth_largest():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert 4 == kthLargest.add(3)
    assert 5 == kthLargest.add(5)
    assert 5 == kthLargest.add(10)
    assert 8 == kthLargest.add(9)
    assert 8 == kthLargest.add(4)
