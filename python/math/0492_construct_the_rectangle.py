import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        m = area
        res = [area, 1]
        for i in range(1, int(math.sqrt(area)) + 1):
            if area % i == 0:
                weight = i
                length = area // weight
                if length - weight < m:
                    res[0] = length
                    res[1] = weight
        return res


def test_construct_rectangle():
    s = Solution()
    assert [2, 2] == s.constructRectangle(4)
    assert [2, 1] == s.constructRectangle(2)
