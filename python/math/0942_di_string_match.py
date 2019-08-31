class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s = 0
        b = len(S)
        r = []
        for c in S:
            if c == 'D':
                r.append(b)
                b -= 1
            if c == 'I':
                r.append(s)
                s += 1
        r.append((s + b) // 2)
        return r


def test_di_string_match():
    s = Solution()
    assert [0, 4, 1, 3, 2] == s.diStringMatch("IDID")
    assert [0, 1, 2, 3] == s.diStringMatch("III")
    assert [3, 2, 0, 1] == s.diStringMatch("DDI")
