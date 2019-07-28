# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        prev_node = head
        node = head.next
        if node is None:
            return head

        head.next = None
        while node.next:
            current = node
            node = node.next
            current.next = prev_node
            prev_node = current
        node.next = prev_node
        return node


def test_reverse_list_1():
    a = ListNode(1)
    s = Solution()
    b = s.reverseList(a)
    assert a.val == b.val


def test_reverse_list_2():
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    s = Solution()
    aa = s.reverseList(a)
    assert aa.val == 2
    assert aa.next.val == 1


def test_reverse_list_3():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    s = Solution()
    aa = s.reverseList(a)
    assert aa.val == 5
    assert aa.next.val == 4
    assert aa.next.next.val == 3
    assert aa.next.next.next.val == 2
    assert aa.next.next.next.next.val == 1
