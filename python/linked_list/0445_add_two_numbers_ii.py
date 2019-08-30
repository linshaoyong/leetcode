# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r1 = self.list_to_array(l1)
        r2 = self.list_to_array(l2)
        rr = []
        carry = 0
        while r1 and r2:
            v = r1.pop() + r2.pop() + carry
            rr.append(v % 10)
            carry = v // 10

        r3 = r1 if r1 else r2
        while r3:
            v = r3.pop() + carry
            rr.append(v % 10)
            carry = v // 10

        if carry == 1:
            rr.append(1)

        prev = ListNode(rr[0])
        for i in range(1, len(rr)):
            current = ListNode(rr[i])
            current.next = prev
            prev = current
        return prev

    def list_to_array(self, ll):
        r = [ll.val]
        while ll.next:
            r.append(ll.next.val)
            ll = ll.next
        return r


def test_add_two_numbers_1():
    a = ListNode(7)
    b = ListNode(2)
    c = ListNode(4)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d

    o = ListNode(5)
    p = ListNode(6)
    q = ListNode(4)
    o.next = p
    p.next = q

    r = Solution().addTwoNumbers(a, o)
    assert 7 == r.val
    assert 8 == r.next.val
    assert 0 == r.next.next.val
    assert 7 == r.next.next.next.val
    assert r.next.next.next.next is None


def test_add_two_numbers_2():
    a = ListNode(5)
    o = ListNode(5)
    r = Solution().addTwoNumbers(a, o)
    assert 1 == r.val
    assert 0 == r.next.val
    assert r.next.next is None
