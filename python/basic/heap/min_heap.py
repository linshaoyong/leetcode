class MinHeap:

    def __init__(self):
        self.data = []

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.data.append(value)
        ci = len(self.data) - 1
        pi = self.parent_index(ci)
        while pi >= 0 and self.data[pi] > self.data[ci]:
            self.data[pi], self.data[ci] = self.data[ci], self.data[pi]
            ci = pi
            pi = self.parent_index(ci)

    def delete(self):
        last = self.data.pop()
        self.data[0] = last

        ci = 0
        while self.has_smaller_child(ci):
            gi = self.calculate_smaller_child_index(ci)
            self.data[gi], self.data[ci] = self.data[ci], self.data[gi]
            ci = gi

    def has_smaller_child(self, index):
        li = self.left_child_index(index)
        ri = self.right_child_index(index)
        if li < len(self.data) and self.data[li] < self.data[index]:
            return True
        if ri < len(self.data) and self.data[ri] < self.data[index]:
            return True
        return False

    def calculate_smaller_child_index(self, index):
        li = self.left_child_index(index)
        ri = self.right_child_index(index)
        if ri >= len(self.data):
            return li
        if self.data[li] < self.data[ri]:
            return li
        return ri


def test_heap_insert():
    heap = MinHeap()
    heap.insert(5)
    assert 5 == heap.root_node()

    heap.insert(8)
    assert 5 == heap.root_node()

    heap.insert(7)
    assert 5 == heap.root_node()

    heap.insert(1)
    assert 1 == heap.root_node()

    heap.insert(9)
    assert 1 == heap.root_node()

    heap.insert(7)
    assert 1 == heap.root_node()


def test_heap_delete():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(8)
    heap.delete()
    assert 8 == heap.root_node()

    heap.insert(1)
    heap.insert(9)
    heap.insert(6)
    heap.insert(5)
    heap.insert(8)

    heap.delete()
    assert 5 == heap.root_node()

    heap.delete()
    assert 6 == heap.root_node()

    heap.delete()
    assert 8 == heap.root_node()

    heap.delete()
    assert 8 == heap.root_node()

    heap.delete()
    assert 9 == heap.root_node()
