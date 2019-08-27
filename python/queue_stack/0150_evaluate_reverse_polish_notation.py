class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for t in tokens:
            if self.is_number(t):
                s.append(t)
            else:
                a = '(' + s.pop() + ')'
                b = '(' + s.pop() + ')'
                s.append(str(int(eval(b + t + a))))
        return int(s.pop())

    def is_number(self, n):
        try:
            float(n)
        except ValueError:
            return False
        return True


def test_eval_RPN():
    s = Solution()
    assert 9 == s.evalRPN(["2", "1", "+", "3", "*"])
    assert 6 == s.evalRPN(["4", "13", "5", "/", "+"])
    assert 22 == s.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
