# Definition for singly-linked list.
class ListNode:
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


def test_merge_two_lists_1():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    a.next = b
    b.next = c

    aa = ListNode(1)
    bb = ListNode(3)
    cc = ListNode(4)
    aa.next = bb
    bb.next = cc

    s = Solution()
    aaa = s.mergeTwoLists(a, aa)
    assert aaa.val == 1
    assert aaa.next.val == 1
    assert aaa.next.next.val == 2
    assert aaa.next.next.next.val == 3
    assert aaa.next.next.next.next.val == 4
    assert aaa.next.next.next.next.next.val == 4


def test_merge_two_lists_2():
    a = ListNode(5)

    aa = ListNode(1)
    bb = ListNode(2)
    cc = ListNode(4)
    aa.next = bb
    bb.next = cc

    s = Solution()
    aaa = s.mergeTwoLists(a, aa)
    assert aaa.val == 1
    assert aaa.next.val == 2
    assert aaa.next.next.val == 4
    assert aaa.next.next.next.val == 5


def test_merge_two_lists_3():
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(5)
    a.next = b
    b.next = c

    aa = ListNode(2)
    bb = ListNode(4)
    aa.next = bb

    s = Solution()
    aaa = s.mergeTwoLists(a, aa)
    assert aaa.val == 1
    assert aaa.next.val == 2
    assert aaa.next.next.val == 3
    assert aaa.next.next.next.val == 4
    assert aaa.next.next.next.next.val == 5


def test_merge_two_lists_4():
    a = ListNode(-9)
    b = ListNode(3)
    a.next = b

    aa = ListNode(5)
    bb = ListNode(7)
    aa.next = bb

    s = Solution()
    aaa = s.mergeTwoLists(a, aa)
    assert aaa.val == -9
    assert aaa.next.val == 3
    assert aaa.next.next.val == 5
    assert aaa.next.next.next.val == 7


def test_merge_two_lists_5():
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

    aa = ListNode(-5)
    bb = ListNode(-3)
    cc = ListNode(0)
    dd = ListNode(7)
    ee = ListNode(8)
    ff = ListNode(8)
    aa.next = bb
    bb.next = cc
    cc.next = dd
    dd.next = ee
    ee.next = ff

    s = Solution()
    aaa = s.mergeTwoLists(a, aa)
    assert aaa.val == -10
    assert aaa.next.val == -9
    assert aaa.next.next.val == -6
    assert aaa.next.next.next.val == -5
    assert aaa.next.next.next.next.val == -4
    assert aaa.next.next.next.next.next.val == -3
    assert aaa.next.next.next.next.next.next.val == 0
    assert aaa.next.next.next.next.next.next.next.val == 1
    assert aaa.next.next.next.next.next.next.next.next.val == 7
    assert aaa.next.next.next.next.next.next.next.next.next.val == 8
    assert aaa.next.next.next.next.next.next.next.next.next.next.val == 8
    assert aaa.next.next.next.next.next.next.next.next.next.next.next.val == 9
    assert aaa.next.next.next.next.next.next.next.next.next.next.next.next.\
        val == 9
