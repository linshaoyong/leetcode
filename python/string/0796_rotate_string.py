class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False


def test_rotate_string():
    s = Solution()
    assert s.rotateString('', '')
    assert s.rotateString('abcde', 'cdeab')
    assert s.rotateString('abcde', 'abced') is False
