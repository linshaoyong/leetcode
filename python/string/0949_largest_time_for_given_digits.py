class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """


def test_largest_time_from_digits():
    s = Solution()
    assert "23:41" == s.largestTimeFromDigits([1, 2, 3, 4])
    assert "" == s.largestTimeFromDigits([5, 5, 5, 5])
