class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        length = len(name)
        i = 0
        for c in typed:
            if c == name[i]:
                i += 1
                if i == length:
                    return True
        return i == length


def test_is_long_pressed_name():
    s = Solution()
    assert s.isLongPressedName("alex", "aaleex")
    assert s.isLongPressedName("saeed", "ssaaedd") is False
    assert s.isLongPressedName("leelee", "lleeelee")
    assert s.isLongPressedName("laiden", "laiden")
    assert s.isLongPressedName("vtkgn", "vttkgnn")
