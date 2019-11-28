class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, ts = [], []
        for c in s:
            if c == ' ':
                continue
            elif c == ')':
                while stack and stack[-1] != '(':
                    ts.append(stack.pop())
                stack.pop()
                ts.reverse()
                stack.append(str(self._cal(ts)))
                ts = []
            else:
                stack.append(c)
        return self._cal(stack)

    def _cal(self, ts):
        v, ccc, add = 0, '', True
        for c in ts:
            if c in ['-', '+']:
                t = int(ccc)
                v = v + t if add else v - t
                add = True if c == '+' else False
                ccc = ''
            else:
                ccc = ccc + c
        return v + int(ccc) if add else v - int(ccc)


def test_calculate():
    s = Solution()
    assert 2 == s.calculate("1 + 1")
    assert 3 == s.calculate(" 2-1 + 2 ")
    assert 23 == s.calculate(" 2-1 + 22 ")
    assert 23 == s.calculate("(1+(4+5+2)-3)+(6+8)")
