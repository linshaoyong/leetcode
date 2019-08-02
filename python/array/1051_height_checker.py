class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sh = sorted(heights)
        r = 0
        for i in range(0, len(heights)):
            if sh[i] != heights[i]:
                r += 1
        return r


def test_heit_checker():
    s = Solution()
    assert 3 == s.heightChecker([1, 1, 4, 2, 1, 3])
