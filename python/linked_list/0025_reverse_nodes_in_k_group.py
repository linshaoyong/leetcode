# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while curr and count != k:
            curr = curr.next
            count += 1

        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                count -= 1
            head = curr
        return head


def test_reverse_k_group_1():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    head = Solution().reverseKGroup(a, 2)
    assert 2 == head.val
    assert 1 == head.next.val
    assert 4 == head.next.next.val
    assert 3 == head.next.next.next.val
    assert 5 == head.next.next.next.next.val


def test_reverse_k_group_2():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    head = Solution().reverseKGroup(a, 3)
    assert 3 == head.val
    assert 2 == head.next.val
    assert 1 == head.next.next.val
    assert 4 == head.next.next.next.val
    assert 5 == head.next.next.next.next.val


def test_reverse_k_group_3():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c

    head = Solution().reverseKGroup(a, 3)
    assert 3 == head.val
    assert 2 == head.next.val
    assert 1 == head.next.next.val
