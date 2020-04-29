class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_ones = s.count('1')
        res, zeros, ones = 0, 0, 0
        for c in s[:-1]:
            if c == '0':
                zeros += 1
            else:
                ones += 1
            res = max(res, zeros + total_ones - ones)
        return res


def test_max_score():
    s = Solution()

    assert 1 == s.maxScore("00")
    assert 5 == s.maxScore("011101")
    assert 5 == s.maxScore("00111")
    assert 3 == s.maxScore("1111")
