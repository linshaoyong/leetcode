class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return root
    def connect(self, root):
        if root:
            a = [root]
            b = []
            while a:
                for n in a:
                    if n.left:
                        b.append(n.left)
                    if n.right:
                        b.append(n.right)
                a = b
                b = []
                for i in range(0, len(a) - 1):
                    a[i].next = a[i + 1]
        return root


def test_connect_1():
    a = TreeLinkNode(1)
    b = TreeLinkNode(2)
    c = TreeLinkNode(3)
    d = TreeLinkNode(4)
    e = TreeLinkNode(5)
    f = TreeLinkNode(6)
    g = TreeLinkNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    a = Solution().connect(a)
    assert a.next is None
    assert a.left.next.val == 3
    assert a.right.next is None

    assert a.left.left.next.val == 5
    assert a.left.right.next.val == 6
    assert a.right.left.next.val == 7
    assert a.right.right.next is None


def test_connect_2():
    a = TreeLinkNode(1)
    b = TreeLinkNode(2)
    c = TreeLinkNode(3)
    d = TreeLinkNode(4)
    e = TreeLinkNode(5)
    f = TreeLinkNode(6)
    g = TreeLinkNode(7)
    h = TreeLinkNode(8)
    i = TreeLinkNode(9)
    j = TreeLinkNode(10)
    k = TreeLinkNode(11)
    ll = TreeLinkNode(12)
    m = TreeLinkNode(13)
    n = TreeLinkNode(14)
    o = TreeLinkNode(15)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    d.left = h
    d.right = i
    e.left = j
    e.right = k
    f.left = ll
    f.right = m
    g.left = n
    g.right = o

    a = Solution().connect(a)
    assert a.next is None
    assert a.left.next.val == 3
    assert a.right.next is None

    assert a.left.left.next.val == 5
    assert a.left.right.next.val == 6
    assert a.right.left.next.val == 7
    assert a.right.right.next is None

    assert a.left.left.left.next.val == 9
    assert a.left.left.right.next.val == 10
    assert a.left.right.left.next.val == 11
    assert a.left.right.right.next.val == 12
    assert a.right.left.left.next.val == 13
    assert a.right.left.right.next.val == 14
    assert a.right.right.left.next.val == 15
    assert a.right.right.right.next is None
