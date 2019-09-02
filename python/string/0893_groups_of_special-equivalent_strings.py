class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = set()
        for a in A:
            aa, bb = [], []
            for i in range(0, len(a)):
                if i % 2 == 0:
                    aa.append(a[i])
                else:
                    bb.append(a[i])
            sa = ''.join(sorted(aa))
            sb = ''.join(sorted(bb))
            res.add((sa, sb,))
        return len(res)


def test_num_special_equiv_groups():
    s = Solution()
    assert 3 == s.numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"])
    assert 4 == s.numSpecialEquivGroups(["aa", "bb", "ab", "ba"])
    assert 3 == s.numSpecialEquivGroups(
        ["abc", "acb", "bac", "bca", "cab", "cba"])
    assert 1 == s.numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"])
