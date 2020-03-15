class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = sorted(s)
        res = []
        while ss:
            ss, taken = self.walk(ss)
            res.extend(taken)
            if ss:
                ss, taken = self.walk(ss[::-1])
                res.extend(taken)
                ss = ss[::-1]
        return ''.join(res)

    def walk(self, source):
        remained = []
        taken = []
        if source:
            taken.append(source[0])
        for v in source[1:]:
            if v == taken[-1]:
                remained.append(v)
            else:
                taken.append(v)
        return remained, taken


def test_sort_string():
    s = Solution()
    assert "abccbaabccba" == s.sortString("aaaabbbbcccc")
    assert "art" == s.sortString("rat")
    assert "cdelotee" == s.sortString("leetcode")
    assert "ggggggg" == s.sortString("ggggggg")
    assert "ops" == s.sortString("spo")
