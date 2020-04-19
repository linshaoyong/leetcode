class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v, s = 1, 1
        for n in nums:
            s += n
            if s < 1:
                v += 1 - s
                s = 1
        return v


def test_min_start_value():
    s = Solution()
    assert 5 == s.minStartValue([-3, 2, -3, 4, 2])
    assert 1 == s.minStartValue([1, 2])
    assert 5 == s.minStartValue([1, -2, -3])
