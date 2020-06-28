class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False

        d = {}
        w = t + 1
        for i in range(len(nums)):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i - k] // w]
        return False


def test_contains_nearby_almost_duplicate():
    s = Solution()
    assert s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
    assert s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
    assert s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) is False
    assert s.containsNearbyAlmostDuplicate([2, 2], 3, 0)
    assert s.containsNearbyAlmostDuplicate([4, 1, -1, 6, 5], 3, 1)
