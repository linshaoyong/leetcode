class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = set(['+', '-', '*', '/'])
        stack_n, stack_s = [], []
        ns = ''
        for c in s:
            if c == ' ':
                continue
            if c in symbols:
                stack_n.append(ns)
                while stack_s and \
                        (c in ['+', '-'] or stack_s[-1] in ['*', '/']):
                    v = self._cal(stack_n.pop(), stack_n.pop(), stack_s.pop())
                    stack_n.append(v)
                stack_s.append(c)
                ns = ''
            else:
                ns += c
        stack_n.append(ns)
        while stack_s:
            v = self._cal(stack_n.pop(), stack_n.pop(), stack_s.pop())
            stack_n.append(v)
        return stack_n[0]

    def _cal(self, a, b, op):
        if op == '+':
            return int(b) + int(a)
        if op == '-':
            return int(b) - int(a)
        if op == '*':
            return int(b) * int(a)
        if op == '/':
            return int(b) // int(a)


def test_calculate():
    s = Solution()
    assert 7 == s.calculate("3+2*2")
    assert 1 == s.calculate(" 3/2 ")
    assert 5 == s.calculate(" 3+5 / 2 ")
    assert 1 == s.calculate("1-1+1")
