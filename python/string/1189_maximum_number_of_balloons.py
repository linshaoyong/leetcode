class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        hm = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for c in text:
            if c in hm:
                hm[c] = hm[c] + 1
        res = hm['b']
        for k, v in hm.items():
            if k == 'l' or k == 'o':
                res = min(res, v // 2)
            else:
                res = min(res, v)
        return res


def test_max_number_of_balloons():
    s = Solution()
    assert 1 == s.maxNumberOfBalloons("nlaebolko")
    assert 2 == s.maxNumberOfBalloons("loonbalxballpoon")
    assert 0 == s.maxNumberOfBalloons("leetcode")
