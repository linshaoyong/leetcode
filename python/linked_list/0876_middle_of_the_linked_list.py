# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head


def test_middle_node_1():
    s = Solution()

    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    e = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    assert c == s.middleNode(a)


def test_middle_node_2():
    s = Solution()

    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    assert d == s.middleNode(a)
