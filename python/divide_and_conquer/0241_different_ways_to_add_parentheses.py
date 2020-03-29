class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """


def test_diff_ways_to_compute():
    s = Solution()
    assert [0, 2] == s.diffWaysToCompute("2-1-1")
    assert [-34, -14, -10, -10, 10] == s.diffWaysToCompute("2*3-4*5")
