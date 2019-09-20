class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        start = -1
        max_zeros = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if i > 0 and seats[i - 1] == 0:
                    zeros = 2 * (i - start - 1) if start < 0 else i - start - 1
                    max_zeros = max(max_zeros, zeros)
                start = i
        max_zeros = max(max_zeros, (len(seats) - 1 - start) * 2)
        return (max_zeros + 1) // 2


def test_max_dist_to_closest():
    s = Solution()
    assert 2 == s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
    assert 3 == s.maxDistToClosest([1, 0, 0, 0])
    assert 3 == s.maxDistToClosest([0, 0, 0, 1])
