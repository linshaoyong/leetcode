class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if coordinates[1][0] == coordinates[0][0]:
            x = coordinates[1][0]
            for coordinate in coordinates:
                if x != coordinate[0]:
                    return False
            return True

        k = (coordinates[1][1] - coordinates[0][1]) / \
            (coordinates[1][0] - coordinates[0][0])
        b = coordinates[0][1] - k * coordinates[0][0]
        for coordinate in coordinates:
            if (k * coordinate[0] + b) != coordinate[1]:
                return False
        return True


def test_check_straight_line():
    s = Solution()
    assert s.checkStraightLine(
        [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    assert s.checkStraightLine(
        [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) is False
