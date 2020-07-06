# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lc, rc = ListNode(0), ListNode(0)
        lch, rch = lc, rc
        while head:
            if head.val < x:
                lc.next = head
                lc = lc.next
            else:
                rc.next = head
                rc = rc.next
            head = head.next
        lc.next = rch.next
        rc.next = None
        return lch.next


def test_partition():
    s = Solution()

    a = ListNode(1, ListNode(4, ListNode(
        3, ListNode(2, ListNode(5, ListNode(2))))))

    b = s.partition(a, 3)
    assert 1 == b.val
    assert 2 == b.next.val
    assert 2 == b.next.next.val
    assert 4 == b.next.next.next.val
    assert 3 == b.next.next.next.next.val
    assert 5 == b.next.next.next.next.next.val
    assert b.next.next.next.next.next.next is None
