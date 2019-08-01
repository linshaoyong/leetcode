# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        head = None
        current = None
        f = 0
        while head1 or head2 or f:
            a = b = 0
            if head1 is not None:
                a = head1.val
                head1 = head1.next
            if head2 is not None:
                b = head2.val
                head2 = head2.next
            c = a + b + f
            f = c // 10
            c = c % 10
            if not head:
                head = ListNode(c)
                current = head
            else:
                current.next = ListNode(c)
                current = current.next
        return head


def test_add_two_numbers_1():
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    a.next = b
    b.next = c

    aa = ListNode(5)
    bb = ListNode(6)
    cc = ListNode(4)
    aa.next = bb
    bb.next = cc

    r = Solution().addTwoNumbers(a, aa)
    assert r.val == 7
    assert r.next.val == 0
    assert r.next.next.val == 8


def test_add_two_numbers_2():
    a = ListNode(1)
    b = ListNode(8)
    a.next = b

    aa = ListNode(0)
    r = Solution().addTwoNumbers(a, aa)
    assert r.val == 1
    assert r.next.val == 8


def test_add_two_numbers_3():
    a = ListNode(5)

    aa = ListNode(5)
    r = Solution().addTwoNumbers(a, aa)
    assert r.val == 0
    assert r.next.val == 1
