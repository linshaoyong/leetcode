class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = sum(A)
        if total % 3 != 0:
            return False
        v = total // 3
        c, s = 0, 0
        for a in A:
            s += a
            if s == v:
                c += 1
                s = 0
        return c > 2


def test_can_three_parts_equal_sum():
    s = Solution()
    assert s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
    assert s.canThreePartsEqualSum(
        [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) is False
    assert s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
