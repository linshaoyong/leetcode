class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sa = sorted(arr)
        diff = sa[1] - sa[0]
        for i in range(2, len(sa)):
            if sa[i] - sa[i - 1] != diff:
                return False
        return True


def test_can_make_arithmetic_progression():
    s = Solution()
    assert s.canMakeArithmeticProgression([3, 5, 1])
    assert s.canMakeArithmeticProgression([1, 2, 4]) is False
