class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minv = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.minv = min(self.minv, x)

    def pop(self):
        """
        :rtype: void
        """
        v = self.stack[-1]
        self.stack = self.stack[:-1]
        if self.stack:
            if v == self.minv:
                self.minv = min(self.stack)
        else:
            self.minv = float('inf')

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minv


def test_min_stack():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3

    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
