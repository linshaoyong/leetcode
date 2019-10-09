class Solution:
    def gardenNoAdj(self, N, paths):
        pass


def test_garden_no_adj():
    s = Solution()
    assert [1, 2, 3] == s.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]])
    assert [1, 1, 2, 3] == s.gardenNoAdj(4, [[3, 4], [4, 2], [3, 2], [1, 3]])
    assert [1, 2, 1, 3, 3] == s.gardenNoAdj(
        5, [[4, 1], [4, 2], [4, 3], [2, 5], [1, 2], [1, 5]])
    assert [1, 2, 2, 1, 3, 2] == s.gardenNoAdj(
        6, [[6, 4], [6, 1], [3, 1], [4, 5], [2, 1], [5, 6], [5, 2]])
