import math

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        r = 0
        for i in range(len(vals)):
            r += vals[i] * math.pow(2, len(vals) - i - 1)
        return int(r)


def test_get_decimal_value():
    s = Solution()

    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)
    assert 5 == s.getDecimalValue(head)

    head = ListNode(1)
    assert 1 == s.getDecimalValue(head)

    head = ListNode(0)
    assert 0 == s.getDecimalValue(head)

    head = ListNode(0)
    head.next = ListNode(0)
    assert 0 == s.getDecimalValue(head)

    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(0)
    head.next.next.next.next.next = ListNode(0)
    head.next.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next.next.next.next = ListNode(0)
    head.next.next.next.next.next.next.next.next.next.next = ListNode(0)
    head.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
    head.next.next.next.next.next.next.next.next.next.next.next.\
        next = ListNode(0)
    head.next.next.next.next.next.next.next.next.next.next.next.\
        next.next = ListNode(0)
    head.next.next.next.next.next.next.next.next.next.next.next.\
        next.next.next = ListNode(0)

    assert 18880 == s.getDecimalValue(head)
