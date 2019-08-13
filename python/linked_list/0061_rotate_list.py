# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i = (len(nodes) - k) % len(nodes)
        if i == 0:
            return nodes[0]
        nodes[i - 1].next = None
        nodes[-1].next = nodes[0]
        return nodes[i]


def test_rotate_right_1():
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    head = s.rotateRight(a, 2)
    assert 4 == head.val
    assert 5 == head.next.val
    assert 1 == head.next.next.val
    assert 2 == head.next.next.next.val
    assert 3 == head.next.next.next.next.val


def test_rotate_right_2():
    s = Solution()
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    a.next = b
    b.next = c

    head = s.rotateRight(a, 4)
    assert 2 == head.val
    assert 0 == head.next.val
    assert 1 == head.next.next.val


def test_rotate_right_3():
    s = Solution()

    head = s.rotateRight(None, 4)
    assert head is None


def test_rotate_right_4():
    s = Solution()
    a = ListNode(0)
    head = s.rotateRight(a, 4)
    assert 0 == head.val


def test_rotate_right_5():
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    head = s.rotateRight(a, 1)
    assert 2 == head.val


def test_rotate_right_6():
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    head = s.rotateRight(a, 0)
    assert 1 == head.val
