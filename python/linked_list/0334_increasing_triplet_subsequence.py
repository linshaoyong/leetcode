class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


def test_increasing_triplet():
    s = Solution()
    assert s.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert s.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert s.increasingTriplet([5, 1, 5, 5, 2, 5, 4]) is True
    assert s.increasingTriplet([2, 4, -2, -3]) is False
