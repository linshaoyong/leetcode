class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [0] * len(s)
        for i, v in enumerate(indices):
            res[v] = s[i]
        return ''.join(res)


def test_resore_string():
    s = Solution()

    assert "leetcode" == s.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
    assert "abc" == s.restoreString("abc", [0, 1, 2])
    assert "nihao" == s.restoreString("aiohn", [3, 1, 4, 2, 0])
    assert "arigatou" == s.restoreString("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5])
    assert "rat" == s.restoreString("art", [1, 0, 2])
