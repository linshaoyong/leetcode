# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        self.traverse(root, stack)
        prev = 0
        while stack:
            node = stack.pop()
            node.val += prev
            prev = node.val
        return root

    def traverse(self, node, stack):
        if node:
            if node.left:
                self.traverse(node.left, stack)
            stack.append(node)
            if node.right:
                self.traverse(node.right, stack)


def test_bst_to_gst():
    a = TreeNode(4)
    b = TreeNode(1)
    c = TreeNode(6)
    d = TreeNode(0)
    e = TreeNode(2)
    f = TreeNode(5)
    g = TreeNode(7)
    h = TreeNode(3)
    i = TreeNode(8)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.right = h
    g.right = i

    a = Solution().bstToGst(a)
    assert 30 == a.val
    assert 36 == a.left.val
    assert 21 == a.right.val
    assert 36 == a.left.left.val
    assert 35 == a.left.right.val
    assert 26 == a.right.left.val
    assert 15 == a.right.right.val
    assert 33 == a.left.right.right.val
    assert 8 == a.right.right.right.val
