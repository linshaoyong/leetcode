class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, m, di = 0, 0, 0, 0
        obs = {tuple(ob) for ob in obstacles}
        for command in commands:
            if command == -1:
                di = (di + 1) % 4
                continue
            if command == -2:
                di = (di + 3) % 4
                continue
            direction = directions[di]
            for i in range(1, command + 1):
                nx, ny = x + direction[0], y + direction[1]
                if (nx, ny) in obs:
                    break
                x, y = nx, ny
            m = max(m, x * x + y * y)
        return m


def test_robot_sim():
    s = Solution()
    assert 25 == s.robotSim([4, -1, 3], [])
    assert 65 == s.robotSim([4, -1, 4, -2, 4], [[2, 4]])
