# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        if a is None:
            return b
        if b is None:
            return a
        head = a if a.val <= b.val else b
        while True:
            if a is None or b is None:
                break
            a, b = self.mergeTwoNodes(a, b)
        return head

    def mergeTwoNodes(self, n1, n2):
        if n1.val <= n2.val:
            c = None
            while n1 is not None and n1.val <= n2.val:
                c = n1
                n1 = n1.next
            if c.next is None:
                c.next = n2
                return None, n2
            c.next = n2
            return self.mergeTwoNodes(n2, n1)
        else:
            return self.mergeTwoNodes(n2, n1)


def test_merge_two_lists():
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(5)
    a.next = b
    b.next = c

    aa = ListNode(2)
    bb = ListNode(4)
    cc = ListNode(6)
    aa.next = bb
    bb.next = cc

    s = Solution()
    aaa = s.mergeTwoLists(a, aa)
    assert 1 == aaa.val
    assert 2 == aaa.next.val
    assert 3 == aaa.next.next.val
    assert 4 == aaa.next.next.next.val
    assert 5 == aaa.next.next.next.next.val
    assert 6 == aaa.next.next.next.next.next.val
