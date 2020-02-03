class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        su_arr = sorted(list(set(arr)))
        m_arr = {su_arr[i]: i + 1 for i in range(len(su_arr))}
        return [m_arr[v] for v in arr]


def test_array_rank_transform():
    s = Solution()
    assert [4, 1, 2, 3] == s.arrayRankTransform([40, 10, 20, 30])
    assert [1, 1, 1] == s.arrayRankTransform([100, 100, 100])
    assert [5, 3, 4, 2, 8, 6, 7, 1, 3] == s.arrayRankTransform(
        [37, 12, 28, 9, 100, 56, 80, 5, 12])
