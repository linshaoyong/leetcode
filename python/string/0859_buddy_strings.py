class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        a, b, sa = [], [], set()
        for i in range(0, len(A)):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
            sa.add(A[i])
        if len(a) == 0:
            if len(A) == len(sa):
                return False
            return True
        if len(a) == 1 or len(a) > 2:
            return False
        return a[0] == b[1] and a[1] == b[0]


def test_buddy_strings():
    s = Solution()
    assert s.buddyStrings("ab", "ba")
    assert s.buddyStrings("ab", "ab") is False
    assert s.buddyStrings("aa", "aa")
    assert s.buddyStrings("aaaaaaabc", "aaaaaaacb")
    assert s.buddyStrings("", "aa") is False
