class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        for v in sorted(nums):
            if v > x:
                return x
            if v == x:
                x += 1
        return x


def test_first_missing_positive():
    s = Solution()

    assert 3 == s.firstMissingPositive([1, 2, 0])
    assert 2 == s.firstMissingPositive([3, 4, -1, 1])
    assert 1 == s.firstMissingPositive([7, 8, 9, 11, 12])
