# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if abs(self.maxDepth(node.left) - self.maxDepth(node.right)) > 1:
                return False
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return True

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        a = [root]
        b = []
        d = 0
        while a:
            for n in a:
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            d += 1
            a = b
            b = []
        return d


def test_is_balanced():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    assert Solution().isBalanced(a)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(3)
    f = TreeNode(4)
    g = TreeNode(4)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.left = f
    d.right = g
    assert Solution().isBalanced(a) is False

    o = TreeNode(1)
    p = TreeNode(2)
    q = TreeNode(3)
    o.right = p
    p.right = q
    assert Solution().isBalanced(o) is False

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    a.left = b
    a.right = c
    d = TreeNode(3)
    e = TreeNode(3)
    f = TreeNode(3)
    g = TreeNode(3)
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    h = TreeNode(4)
    i = TreeNode(4)
    j = TreeNode(4)
    k = TreeNode(4)
    ll = TreeNode(4)
    m = TreeNode(4)
    d.left = h
    d.right = i
    e.left = j
    e.right = k
    f.left = ll
    f.right = m
    n = TreeNode(5)
    o = TreeNode(5)
    h.left = n
    h.right = o
    assert Solution().isBalanced(a)
