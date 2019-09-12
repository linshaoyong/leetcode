# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, _next=None):
        self.val = x
        self.next = _next


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res, stack, i = [], [], 0
        while head:
            res.append(0)
            while stack and stack[-1][0] < head.val:
                _, index = stack.pop()
                res[index] = head.val
            stack.append((head.val, i,))
            head = head.next
            i += 1
        return res


def test_next_larger_nodes():
    s = Solution()
    a = ListNode(2, ListNode(1, ListNode(5)))
    assert [5, 5, 0] == s.nextLargerNodes(a)

    a = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))
    assert [7, 0, 5, 5, 0] == s.nextLargerNodes(a)

    a = ListNode(1, ListNode(7, ListNode(5, ListNode(
        1, ListNode(9, ListNode(2, ListNode(5, ListNode(1))))))))
    assert [7, 9, 9, 9, 0, 5, 0, 0] == s.nextLargerNodes(a)
