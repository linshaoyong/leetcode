class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.backspace(S) == self.backspace(T)

    def backspace(self, s):
        res = []
        for c in s:
            if c == '#':
                if res:
                    res.pop()
            else:
                res.append(c)
        return res


def test_backspace_compare():
    s = Solution()
    assert s.backspaceCompare("ab#c", "ad#c")
    assert s.backspaceCompare("ab##", "c#d#")
    assert s.backspaceCompare("a##c", "#a#c")
    assert s.backspaceCompare("a#c", "b") is False
