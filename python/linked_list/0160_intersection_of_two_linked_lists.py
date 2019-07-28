# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa


def test_get_intersection_node():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(6)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    aa = ListNode(2)
    bb = ListNode(1)
    cc = ListNode(3)
    aa.next = bb
    bb.next = cc
    cc.next = d

    r = Solution().getIntersectionNode(a, aa)
    assert r.val == 4
    assert r.next.val == 5
    assert r.next.next is None
