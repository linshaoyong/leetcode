class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k
        self.container = [-1 for _ in range(0, k)]
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue.
        Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.head = self.tail = 0
            self.container[0] = value
            return True
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.k
        self.container[self.tail] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue.
        Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
            return True
        self.head = (self.head + 1) % self.k
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.container[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.container[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.head < 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.head >= 0:
            if abs(self.head - self.tail) == (self.k - 1) or (self.head - self.tail) == 1:
                return True
        return False


def test_circular_queue():
    q = MyCircularQueue(3)

    assert q.isEmpty()
    assert q.isFull() is False
    assert q.enQueue(1)
    assert q.isEmpty() is False

    assert q.isFull() is False
    assert q.enQueue(2)
    assert q.isEmpty() is False

    assert q.isFull() is False
    assert q.enQueue(3)
    assert q.isEmpty() is False

    assert q.isFull()
    assert q.enQueue(4) is False

    assert 1 == q.Front()
    assert 3 == q.Rear()

    assert q.deQueue()
    assert q.isFull() is False

    assert q.enQueue(4)
    assert q.isFull()

    assert 2 == q.Front()
    assert 4 == q.Rear()
