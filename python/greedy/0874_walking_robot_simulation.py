class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """


def test_robot_sim():
    s = Solution()
    assert 25 == s.robotSim([4, -1, 3], [])
    assert 65 == s.robotSim([4, -1, 4, -2, 4], [[2, 4]])
