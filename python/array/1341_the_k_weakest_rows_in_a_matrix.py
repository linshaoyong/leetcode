class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(mat)):
            soldiers = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    break
                soldiers += 1
            res.append((soldiers, i))

        res.sort()
        return [i for _, i in res[:k]]


def test_k_weakest_rows():
    s = Solution()
    assert [2, 0, 3] == s.kWeakestRows([[1, 1, 0, 0, 0],
                                        [1, 1, 1, 1, 0],
                                        [1, 0, 0, 0, 0],
                                        [1, 1, 0, 0, 0],
                                        [1, 1, 1, 1, 1]], 3)

    assert [0, 2] == s.kWeakestRows([[1, 0, 0, 0],
                                     [1, 1, 1, 1],
                                     [1, 0, 0, 0],
                                     [1, 0, 0, 0]], 2)
