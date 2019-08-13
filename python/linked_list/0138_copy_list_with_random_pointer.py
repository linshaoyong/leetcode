# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)


def test_copy_random_list():
    s = Solution()

    a = Node(1, None, None)
    b = Node(2, None, None)
    b.random = b
    a.random = b
    a.next = b

    aa = s.copyRandomList(a)
    assert 1 == aa.val
    assert 2 == aa.next.val
    assert 2 == aa.random.val
    assert 2 == aa.next.random.val
