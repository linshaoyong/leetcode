class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        curr = self.head
        for i in range(1, index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the
        linked list.
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        curr = self.head
        while curr.next:
            curr = curr.next
        new_node = ListNode(val)
        curr.next = new_node
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node

        if index <= self.length:
            prev = None
            curr = self.head
            for i in range(1, index + 1):
                prev = curr
                curr = curr.next
            new_node = ListNode(val)
            if prev:
                prev.next = new_node
            else:
                self.head = new_node
            new_node.next = curr
            self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= 0 and index < self.length:
            prev = None
            curr = self.head
            _next = None
            if curr:
                _next = curr.next
            for i in range(1, index + 1):
                prev = curr
                curr = curr.next
                if curr:
                    _next = curr.next
            if prev:
                prev.next = _next
            else:
                self.head = _next
            self.length -= 1


def test_my_linked_list_1():
    ll = MyLinkedList()
    ll.addAtHead(1)
    assert 1 == ll.get(0)

    ll.addAtTail(3)
    assert -1 == ll.get(-1)
    assert 1 == ll.get(0)
    assert 3 == ll.get(1)

    ll.addAtIndex(1, 2)
    assert 1 == ll.get(0)
    assert 2 == ll.get(1)
    assert 3 == ll.get(2)

    ll.deleteAtIndex(1)
    assert 3 == ll.get(1)
    assert -1 == ll.get(-3)


def test_my_linked_list_2():
    ll = MyLinkedList()
    ll.addAtHead(1)
    assert 1 == ll.get(0)

    ll.addAtIndex(1, 2)
    assert 1 == ll.get(0)
    assert 2 == ll.get(1)
    assert -1 == ll.get(2)


def test_my_linked_list_3():
    ll = MyLinkedList()
    ll.addAtHead(1)
    assert 1 == ll.get(0)

    ll.addAtTail(3)
    assert -1 == ll.get(-1)
    assert 1 == ll.get(0)
    assert 3 == ll.get(1)

    ll.addAtIndex(4, 2)
    assert 3 == ll.get(1)

    ll.deleteAtIndex(-1)
    assert 3 == ll.get(1)


def test_my_linked_list_4():
    ll = MyLinkedList()
    ll.addAtIndex(-1, 0)
    assert 0 == ll.get(0)
