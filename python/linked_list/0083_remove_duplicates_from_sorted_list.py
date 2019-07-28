# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def walk(self, node):
        if node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
                self.walk(node)
            else:
                self.walk(node.next)

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.walk(head)
        return head


def test_delete_duplicates():

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    s = Solution()
    aa = s.deleteDuplicates(a)
    assert aa.val == 1
    assert aa.next.val == 2
    assert aa.next.next.val == 3
