class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


def test_max_area():
    s = Solution()
    assert 49 == s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert 25 == s.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
