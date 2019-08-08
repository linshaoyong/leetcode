# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        element = head
        s = set()
        while element:
            if element in s:
                return element
            s.add(element)
            element = element.next
        return None


def test_detect_cycle():
    s = Solution()

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
    assert cc == s.detectCycle(aa)
