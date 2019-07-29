# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        element = head
        s = set()
        while element:
            if element in s:
                return True
            s.add(element)
            element = element.next
        return False


def test_has_cycle():
    s = Solution()

    a = ListNode(-10)
    b = ListNode(-9)
    c = ListNode(-6)
    d = ListNode(-4)
    e = ListNode(1)
    f = ListNode(9)
    g = ListNode(9)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    assert s.hasCycle(a) is False

    aa = ListNode(-10)
    bb = ListNode(-9)
    cc = ListNode(-6)
    dd = ListNode(-4)
    ee = ListNode(1)
    aa.next = bb
    bb.next = cc
    cc.next = dd
    dd.next = ee
    ee.next = cc
    assert s.hasCycle(aa) is True
