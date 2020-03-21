class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = {S[i]: i for i in range(len(S))}
        return ''.join(sorted(T, key=lambda s: m.get(s, ord(s))))


def test_custom_sort_string():
    s = Solution()
    assert "cbad" == s.customSortString("cba", "abcd")
    assert "kqeep" == s.customSortString("kqep", "pekeq")
