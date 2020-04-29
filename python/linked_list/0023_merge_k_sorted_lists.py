import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class CmpNode:

    def __init__(self, node):
        self.node = node
        self.val = node.val

    def __gt__(self, another):
        return self.val > another.val


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for node in lists:
            if node:
                heapq.heappush(h, CmpNode(node))
        if not h:
            return None

        head, prev = None, None
        while h:
            cmpn = heapq.heappop(h)
            if not head:
                head = cmpn.node
                prev = head
            else:
                prev.next = cmpn.node
                prev = cmpn.node

            if cmpn.node.next:
                heapq.heappush(h, CmpNode(cmpn.node.next))
        return head


def test_merge_k_lists_1():
    s = Solution()

    a = ListNode(1, ListNode(4, ListNode(5)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    c = ListNode(2, ListNode(6))

    r = s.mergeKLists([a, b, c])
    assert 1 == r.val
    assert 1 == r.next.val
    assert 2 == r.next.next.val
    assert 3 == r.next.next.next.val
    assert 4 == r.next.next.next.next.val
    assert 4 == r.next.next.next.next.next.val
    assert 5 == r.next.next.next.next.next.next.val
    assert 6 == r.next.next.next.next.next.next.next.val
    assert r.next.next.next.next.next.next.next.next is None
