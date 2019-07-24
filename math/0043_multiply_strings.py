class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """


def test_multiply():
    s = Solution()
    assert "6" == s.multiply("2", "3")
    assert "56088" == s.multiply("123", "456")
