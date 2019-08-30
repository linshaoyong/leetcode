class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        q = [x]
        while self.data:
            q.append(self.data.pop(0))
        self.data = q

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.data.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.data) == 0


def test_mystack():

    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert 2 == stack.top()
    assert 2 == stack.pop()
    assert stack.empty() is False
