class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        ss = [s[i] for i in range(len(s) - 1, -1, -1)]
        for c in t:
            if c == ss[-1]:
                ss.pop()
                if len(ss) == 0:
                    return True
        return False


def test_is_sub_sequence():
    s = Solution()
    assert s.isSubsequence("abc", "ahbgdc")
    assert s.isSubsequence("axc", "ahbgdc") is False
    assert s.isSubsequence("acb", "ahbgdc") is False
    assert s.isSubsequence("", "ahbgdc")
    assert s.isSubsequence("c", "b") is False
