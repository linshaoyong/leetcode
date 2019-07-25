class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = {}
        for v in magazine:
            m[v] = m.get(v, 0) + 1
        for v in ransomNote:
            m[v] = m.get(v, 0) - 1
            if m[v] < 0:
                return False
        return True


def test_can_construct():
    s = Solution()

    assert s.canConstruct("a", "b") is False
    assert s.canConstruct("aa", "ab") is False
    assert s.canConstruct("aa", "aab") is True
