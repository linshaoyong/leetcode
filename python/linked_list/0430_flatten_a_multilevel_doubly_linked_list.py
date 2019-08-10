# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):

    def flatten(self, head):
        if not head:
            return

        dummy = Node(0, None, head, None)
        stack = []
        stack.append(head)
        prev = dummy

        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root

        dummy.next.prev = None
        return dummy.next


def test_flatten():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    c.next = d
    d.prev = c
    d.next = e
    e.prev = d
    e.next = f
    f.prev = e

    g = Node(7)
    h = Node(8)
    i = Node(9)
    j = Node(10)
    c.child = g
    g.next = h
    h.prev = g
    h.next = i
    i.prev = h
    i.next = j
    j.prev = i

    k = Node(11)
    ll = Node(12)
    h.child = k
    k.next = ll
    ll.prev = h

    s = Solution()
    a = s.flatten(a)

    assert 1 == a.val
    assert 2 == a.next.val
    assert 3 == a.next.next.val
    assert 7 == a.next.next.next.val
    assert 8 == a.next.next.next.next.val
    assert 11 == a.next.next.next.next.next.val
    assert 12 == a.next.next.next.next.next.next.val
    assert 9 == a.next.next.next.next.next.next.next.val
    assert 10 == a.next.next.next.next.next.next.next.next.val
    assert 4 == a.next.next.next.next.next.next.next.next.next.val
    assert 5 == a.next.next.next.next.next.next.next.next.next.next.val
    assert 6 == a.next.next.next.next.next.next.next.next.next.next.next.val
