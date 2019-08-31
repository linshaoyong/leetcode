class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        s = {candy for candy in candies}
        return min(len(s), len(candies) // 2)


def test_distribute_candies():
    s = Solution()
    assert 3 == s.distributeCandies([1, 1, 2, 2, 3, 3])
    assert 2 == s.distributeCandies([1, 1, 2, 3])
