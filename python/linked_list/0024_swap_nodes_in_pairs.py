# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        n = head.next
        head.next = self.swapPairs(n.next)
        n.next = head
        return n


def test_swap_pairs():
    s = Solution()

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    head = s.swapPairs(a)
    assert 2 == head.val
    assert 1 == head.next.val
    assert 4 == head.next.next.val
    assert 3 == head.next.next.next.val
