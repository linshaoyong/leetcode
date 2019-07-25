class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        return False


def test_contains_nearby_almost_duplicate():
    s = Solution()
    assert s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0) is True
    assert s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2) is True
    assert s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) is False
    assert s.containsNearbyAlmostDuplicate([4, 1, -1, 6, 5], 3, 1) is True
