# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(parent, node, is_left):
            if node:
                traverse(node, node.left, True)
                traverse(node, node.right, False)
                if node.val == 0:
                    if node.left is None and node.right is None:
                        if is_left:
                            parent.left = None
                        else:
                            parent.right = None

        traverse(root, root.left, True)
        traverse(root, root.right, False)
        return None if root.val == 0 and \
            root.left is None and root.right is None else root


def test_prune_tree_1():
    a = TreeNode(1)
    b = TreeNode(0)
    c = TreeNode(0)
    d = TreeNode(1)
    a.right = b
    b.left = c
    b.right = d

    a = Solution().pruneTree(a)
    assert 1 == a.val
    assert a.left is None
    assert 0 == a.right.val
    assert a.right.left is None
    assert 1 == a.right.right.val


def test_prune_tree_2():
    a = TreeNode(1)
    b = TreeNode(0)
    c = TreeNode(1)
    d = TreeNode(0)
    e = TreeNode(0)
    f = TreeNode(0)
    g = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    a = Solution().pruneTree(a)
    assert 1 == a.val
    assert a.left is None
    assert 1 == a.right.val
    assert a.right.left is None
    assert 1 == a.right.right.val


def test_prune_tree_3():
    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(0)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(0)
    g = TreeNode(1)
    h = TreeNode(0)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h

    a = Solution().pruneTree(a)
    assert 1 == a.val
    assert 1 == a.left.val
    assert 0 == a.right.val
    assert 1 == a.left.left.val
    assert a.left.left.left is None
    assert 1 == a.left.right.val
    assert a.right.left is None
    assert 1 == a.right.right.val
