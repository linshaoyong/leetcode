class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for a in s:
            if not res:
                res.append(a)
                continue
            if abs(ord(res[-1]) - ord(a)) == 32:
                res.pop()
            else:
                res.append(a)
        return "".join(res)


def test_make_good():
    s = Solution()
    assert "leetcode" == s.makeGood("leEeetcode")
    assert "" == s.makeGood("abBAcC")
    assert "s" == s.makeGood("s")
    assert "Mc" == s.makeGood("Mc")
