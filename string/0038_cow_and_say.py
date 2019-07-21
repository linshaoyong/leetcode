class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """


def test_countAndSay():
    s = Solution()
    assert "1" == s.countAndSay(1)
    assert "1211" == s.countAndSay(4)
