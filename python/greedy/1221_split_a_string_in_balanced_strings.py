class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        rs, ls = 0, 0
        for c in s:
            if c == 'R':
                rs += 1
            else:
                ls += 1
            if rs == ls:
                res += 1
        return res


def test_balanced_string_split():
    s = Solution()
    assert 4 == s.balancedStringSplit("RLRRLLRLRL")
    assert 3 == s.balancedStringSplit("RLLLLRRRLR")
    assert 1 == s.balancedStringSplit("LLLLRRRR")
    assert 2 == s.balancedStringSplit("RRLRRLRLLLRL")
