class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphas = [a for a in s if a.isalpha()]
        nums = [a for a in s if a.isnumeric()]
        if abs(len(alphas) - len(nums)) > 1:
            return ""

        longs = alphas if len(alphas) >= len(nums) else nums
        shorts = nums if len(alphas) >= len(nums) else alphas

        res = []
        for i in range(len(longs)):
            res.append(longs[i])
            if i < len(shorts):
                res.append(shorts[i])
        return ''.join(res)


def test_reformat():
    s = Solution()
    assert "a0b1c2" == s.reformat("a0b1c2")
    assert "" == s.reformat("leetcode")
    assert "" == s.reformat("1229857369")
    assert "c2o0v1i9d" == s.reformat("covid2019")
    assert "1a2b3" == s.reformat("ab123")
