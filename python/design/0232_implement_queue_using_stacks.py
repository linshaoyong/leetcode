class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        stack = [x]
        tmp = []
        while self.data:
            tmp.append(self.data.pop())
        while tmp:
            stack.append(tmp.pop())
        self.data = stack

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.data.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.data[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.data) == 0


def test_myqueue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert 1 == q.peek()
    assert 1 == q.pop()
    assert q.empty() is False
