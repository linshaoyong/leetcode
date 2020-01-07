class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.cache = {}

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i, j,) not in self.cache:
            self.cache[(i, j,)] = sum(self.nums[i:j + 1])
        return self.cache[(i, j,)]


def test_num_array():
    o = NumArray([-2, 0, 3, -5, 2, -1])
    assert 1 == o.sumRange(0, 2)
    assert -1 == o.sumRange(2, 5)
    assert -3 == o.sumRange(0, 5)
