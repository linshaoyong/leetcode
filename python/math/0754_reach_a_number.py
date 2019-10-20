class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """


def test_reach_number():
    s = Solution()
    assert 2 == s.reachNumber(3)
    assert 3 == s.reachNumber(2)
    assert 3 == s.reachNumber(4)
