class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        hd = {}
        for domino in dominoes:
            sd = sorted(domino)
            dd = (sd[0], sd[1],)
            hd[dd] = hd.get(dd, 0) + 1

        res = 0
        for _, v in hd.items():
            if v < 2:
                continue
            res += v * (v - 1) / 2
        return res


def test_num_equiv_domino_pairs():
    assert 1 == Solution().numEquivDominoPairs(
        [[1, 2], [2, 1], [3, 4], [5, 6]])

    assert 3 == Solution().numEquivDominoPairs(
        [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]])
