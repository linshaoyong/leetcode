class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        x = max(candies) - extraCandies
        return [True if c >= x else False for c in candies]


def test_kids_with_candies():
    s = Solution()

    assert [True, True, True, False, True] == s.kidsWithCandies(
        [2, 3, 5, 1, 3], 3)
    assert [True, False, False, False,
            False] == s.kidsWithCandies([4, 2, 1, 1, 2], 1)
    assert [True, False, True] == s.kidsWithCandies([12, 1, 12], 10)
