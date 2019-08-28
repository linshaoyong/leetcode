# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        res = []
        self.traversal(root, res)
        prev = res[0]
        prev.left = None
        for n in res[1:]:
            n.left = None
            prev.right = n
            prev = n
        return res[0]

    def traversal(self, node, res):
        if node:
            self.traversal(node.left, res)
            res.append(node)
            self.traversal(node.right, res)


def test_increasing_bst():
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(8)
    g = TreeNode(1)
    h = TreeNode(7)
    i = TreeNode(9)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    d.left = g
    f.left = h
    f.right = i

    root = Solution().increasingBST(a)
    assert 1 == root.val
    assert root.left is None
    assert 2 == root.right.val
    assert root.right.left is None
    assert 3 == root.right.right.val
    assert root.right.right.left is None
    assert 4 == root.right.right.right.val
    assert root.right.right.right.left is None
    assert 5 == root.right.right.right.right.val
    assert root.right.right.right.right.left is None
    assert 6 == root.right.right.right.right.right.val
    assert root.right.right.right.right.right.left is None
    assert 7 == root.right.right.right.right.right.right.val
    assert root.right.right.right.right.right.right.left is None
    assert 8 == root.right.right.right.right.right.right.right.val
    assert root.right.right.right.right.right.right.right.left is None
    assert 9 == root.right.right.right.right.right.right.right.right.val
    assert root.right.right.right.right.right.right.right.right.left is None
