class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        j = 0
        for i in range(0, len(nums)):
            if m == nums[i]:
                if j == 0:
                    j = i
                continue
            if m < 2 * nums[i]:
                return -1
        return j


def test_dominant_index():
    s = Solution()
    assert 1 == s.dominantIndex([3, 6, 1, 0])
    assert -1 == s.dominantIndex([1, 2, 3, 4])
    assert 3 == s.dominantIndex([0, 0, 0, 1])
