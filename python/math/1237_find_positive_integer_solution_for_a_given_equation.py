class CustomFunction:
    def f(self, x, y):
        return x + y


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        x, go_on, maxv = 1, True, 1001
        while x < maxv and go_on:
            for y in range(1, maxv):
                if customfunction.f(x, y) >= z:
                    if customfunction.f(x, y) == z:
                        res.append([x, y])
                    if y == 1:
                        go_on = False
                    break
            x += 1
        return res


def test_find_solution():
    s = Solution()

    assert [[1, 4], [2, 3], [3, 2], [4, 1]
            ] == s.findSolution(CustomFunction(), 5)
