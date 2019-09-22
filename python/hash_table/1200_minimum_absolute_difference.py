class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        if len(arr) < 2:
            return []
        sa = sorted(arr)
        min_diff = sa[1] - sa[0]
        res = [[sa[0], sa[1]]]
        for i in range(1, len(sa) - 1):
            v = sa[i + 1] - sa[i]
            if v < min_diff:
                res = [[sa[i], sa[i + 1]]]
                min_diff = v
                continue
            if v == min_diff:
                res.append([sa[i], sa[i + 1]])
        return res


def test_minimum_abs_difference():
    s = Solution()
    assert [[1, 2], [2, 3], [3, 4]] == s.minimumAbsDifference([4, 2, 1, 3])
    assert [[1, 3]] == s.minimumAbsDifference([1, 3, 6, 10, 15])
    assert [[-14, -10], [19, 23], [23, 27]
            ] == s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27])
