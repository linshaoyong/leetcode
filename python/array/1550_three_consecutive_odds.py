class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        odds = 0
        for a in arr:
            if a % 2 == 1:
                odds += 1
                if odds >= 3:
                    return True
            else:
                odds = 0
        return False


def test_three_consecutive_odds():
    s = Solution()

    assert s.threeConsecutiveOdds([2, 6, 4, 1]) is False
    assert s.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12])
