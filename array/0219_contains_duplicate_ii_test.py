class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for i in range(0, len(nums)):
            if len(s) < k + 1:
                if nums[i] in s:
                    return True
                s.add(nums[i])
                continue
            s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False


def test_contains_nearby_duplicate():
    s = Solution()
    assert s.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert s.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
