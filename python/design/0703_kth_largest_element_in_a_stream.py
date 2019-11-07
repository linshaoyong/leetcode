import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


def test_kth_largest_1():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert 4 == kthLargest.add(3)
    assert 5 == kthLargest.add(5)
    assert 5 == kthLargest.add(10)
    assert 8 == kthLargest.add(9)
    assert 8 == kthLargest.add(4)


def test_kth_largest_2():
    kthLargest = KthLargest(1, [])
    assert -3 == kthLargest.add(-3)
    assert -2 == kthLargest.add(-2)
    assert -2 == kthLargest.add(-4)
    assert 0 == kthLargest.add(0)
    assert 4 == kthLargest.add(4)
