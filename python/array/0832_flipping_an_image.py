class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(0, len(A)):
            row = A[i]
            length = len(row)
            mid = length // 2
            for j in range(0, mid):
                row[j] = 1 - row[j]
                row[length - 1 - j] = 1 - row[length - 1 - j]
                row[j], row[length - 1 - j] = row[length - 1 - j], row[j]
            if length % 2 == 1:
                row[mid] = 1 - row[mid]
        return A


def test_flip_and_invert_image():
    s = Solution()
    assert [[1, 0, 0],
            [0, 1, 0],
            [1, 1, 1]] == s.flipAndInvertImage(
        [[1, 1, 0],
         [1, 0, 1],
         [0, 0, 0]])

    assert [[1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 1, 0]] == s.flipAndInvertImage(
                [[1, 1, 0, 0],
                 [1, 0, 0, 1],
                 [0, 1, 1, 1],
                 [1, 0, 1, 0]])
