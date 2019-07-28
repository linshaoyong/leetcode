class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key=lambda x: x % 2 != 0)


def test_sort_array_by_parity():
    s = Solution()
    r = s.sortArrayByParity([3, 1, 2, 4])
    assert 2 in r[:2]
    assert 4 in r[:2]
    assert 3 in r[2:]
    assert 1 in r[2:]
