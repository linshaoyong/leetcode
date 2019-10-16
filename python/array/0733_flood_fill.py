class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        v = image[sr][sc]
        if v == newColor:
            return image

        image[sr][sc] = newColor
        stack = [(sr, sc)]
        while stack:
            i, j = stack.pop()
            if i > 0 and image[i - 1][j] == v:
                stack.append((i - 1, j,))
                image[i - 1][j] = newColor

            if i < len(image) - 1 and image[i + 1][j] == v:
                stack.append((i + 1, j,))
                image[i + 1][j] = newColor

            if j > 0 and image[i][j - 1] == v:
                stack.append((i, j - 1,))
                image[i][j - 1] = newColor

            if j < len(image[0]) - 1 and image[i][j + 1] == v:
                stack.append((i, j + 1,))
                image[i][j + 1] = newColor
        return image


def test_flood_fill():
    s = Solution()
    assert [[2, 2, 2], [2, 2, 0], [2, 0, 1]] == s.floodFill(
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
