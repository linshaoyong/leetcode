class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        v = 0
        res = []
        for a in A:
            v = (v << 1) + a
            if v % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res


def test_prefixes_div_by_five():
    s = Solution()
    assert [True, False, False] == s.prefixesDivBy5([0, 1, 1])
    assert [False, False, False] == s.prefixesDivBy5([1, 1, 1])
    assert [True, False, False, False, True,
            False] == s.prefixesDivBy5([0, 1, 1, 1, 1, 1])
    assert [False, False, False, False,
            False] == s.prefixesDivBy5([1, 1, 1, 0, 1])
