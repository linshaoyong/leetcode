# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        odd = head
        even = even_head = head.next
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


def test_0():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    r = Solution().oddEvenList(a)
    assert r.val == 1
    assert r.next.val == 3
    assert r.next.next.val == 5
    assert r.next.next.next.val == 2
    assert r.next.next.next.next.val == 4


def test_1():
    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)
    g = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    r = Solution().oddEvenList(a)
    assert r.val == 2
    assert r.next.val == 3
    assert r.next.next.val == 6
    assert r.next.next.next.val == 7
    assert r.next.next.next.next.val == 1
    assert r.next.next.next.next.next.val == 5
    assert r.next.next.next.next.next.next.val == 4
