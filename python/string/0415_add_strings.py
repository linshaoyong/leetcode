class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry:
            res.append(carry)
        return ''.join([str(i) for i in res])[::-1]


def test_add_strings():
    s = Solution()
    assert "0" == s.addStrings("0", "0")
    assert "1" == s.addStrings("0", "1")
    assert "357" == s.addStrings("123", "234")
    assert "124023" == s.addStrings("123789", "234")
