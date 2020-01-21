class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """


def test_num_rolls_to_target():
    s = Solution()
    assert 1 == s.numRollsToTarget(1, 6, 3)
    assert 6 == s.numRollsToTarget(2, 6, 7)
    assert 1 == s.numRollsToTarget(2, 5, 10)
    assert 0 == s.numRollsToTarget(1, 2, 3)
    assert 222616187 == s.numRollsToTarget(30, 30, 500)
