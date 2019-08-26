class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        s2 = set(arr2)
        not_exists = []
        exists = {}
        for c in arr1:
            if c not in s2:
                not_exists.append(c)
            else:
                exists[c] = exists.get(c, 0) + 1
        r = []
        for c in arr2:
            for _ in range(0, exists.get(c)):
                r.append(c)
        return r + sorted(not_exists)


def test_relative_sort_array():
    s = Solution()
    assert [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19] == s.relativeSortArray(
        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
