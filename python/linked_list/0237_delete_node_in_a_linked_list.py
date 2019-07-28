# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def test_delete_node():
    a = ListNode(4)
    b = ListNode(5)
    c = ListNode(1)
    d = ListNode(9)
    a.next = b
    b.next = c
    c.next = d

    s = Solution()
    s.deleteNode(b)

    assert a.val == 4
    assert a.next.val == 1
    assert a.next.next.val == 9
