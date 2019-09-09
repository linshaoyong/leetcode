class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
                continue
            if op == 'D':
                v = stack[-1] * 2
                stack.append(v)
                continue
            if op == '+':
                v = stack[-1] + stack[-2]
                stack.append(v)
                continue
            stack.append(int(op))
        return sum(stack)


def test_cal_points():
    s = Solution()
    assert 30 == s.calPoints(["5", "2", "C", "D", "+"])
    assert 27 == s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
