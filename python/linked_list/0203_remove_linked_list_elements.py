# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = None
        prev = None
        current = head
        while current:
            if current.val == val:
                if prev:
                    prev.next = current.next
            else:
                if not new_head:
                    new_head = current
                prev = current
            current = current.next
        return new_head


def test_remove_elements_1():
    s = Solution()

    a = ListNode(1)
    b = ListNode(2)
    a.next = b

    head = s.removeElements(a, 1)
    assert 2 == head.val
    assert head.next is None


def test_remove_elements_2():
    s = Solution()

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(6)
    d = ListNode(3)
    e = ListNode(4)
    f = ListNode(5)
    g = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    s.removeElements(a, 6)
    assert 1 == a.val
    assert 2 == a.next.val
    assert 3 == a.next.next.val
    assert 4 == a.next.next.next.val
    assert 5 == a.next.next.next.next.val
