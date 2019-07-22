class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"


def test_countAndSay():
    s = Solution()
    assert "1" == s.countAndSay(1)
    assert "11" == s.countAndSay(2)
    assert "21" == s.countAndSay(3)
    assert "1211" == s.countAndSay(4)
