# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        node = head
        nodes.append(node)
        while node.next:
            nodes.append(node.next)
            node = node.next
        nums = len(nodes)
        if n == nums:
            return head.next
        nodes[nums - n - 1].next = nodes[nums - n].next
        return nodes[0]


def test_remove_nth_from_end_1():
    a = ListNode(1)
    s = Solution()
    head = s.removeNthFromEnd(a, 1)
    assert head is None


def test_remove_nth_from_end_2():
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    s = Solution()
    head = s.removeNthFromEnd(a, 2)
    assert head.val == 2
    assert head.next is None


def test_remove_nth_from_end_3():
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
    head = s.removeNthFromEnd(a, 2)
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 3
    assert head.next.next.next.val == 5
