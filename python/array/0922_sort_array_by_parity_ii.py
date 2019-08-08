class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odds, evens = [], []
        for i in range(0, len(A)):
            if i % 2 == 0 and A[i] % 2 != 0:
                evens.append(i)
                continue
            if i % 2 != 0 and A[i] % 2 == 0:
                odds.append(i)
        for i in range(0, len(odds)):
            A[odds[i]], A[evens[i]] = A[evens[i]], A[odds[i]]
        return A


def test_sort_array_by_parity_ii():
    s = Solution()
    r = s.sortArrayByParityII([3, 1, 2, 4])
    assert r[0] in [2, 4]
    assert r[1] in [1, 3]
    assert r[2] in [2, 4]
    assert r[3] in [1, 3]
