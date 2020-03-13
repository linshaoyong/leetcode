# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        self.traverse(root.left, root, target, True)
        self.traverse(root.right, root, target, False)

        if root.val == target and root.left is None and root.right is None:
            return None
        return root

    def traverse(self, node, pnode, target, left):
        if node:
            if node.left:
                self.traverse(node.left, node, target, True)
            if node.right:
                self.traverse(node.right, node, target, False)
            if node.val == target:
                if node.left is None and node.right is None:
                    if left:
                        pnode.left = None
                    else:
                        pnode.right = None


def test_removeLeafNodes_1():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(2)
    e = TreeNode(2)
    f = TreeNode(4)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f

    s = Solution()
    r = s.removeLeafNodes(a, 2)
    assert r.val == 1
    assert r.left is None
    assert r.right.val == 3
    assert r.right.left is None
    assert r.right.right.val == 4


def test_removeLeafNodes_2():
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(3)
    d = TreeNode(3)
    e = TreeNode(2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    s = Solution()
    r = s.removeLeafNodes(a, 3)
    assert r.val == 1
    assert r.right is None
    assert r.left.val == 3
    assert r.left.left is None
    assert r.left.right.val == 2


def test_removeLeafNodes_3():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(2)
    a.left = b
    b.left = c
    c.left = d

    s = Solution()
    r = s.removeLeafNodes(a, 2)
    assert r.val == 1
    assert r.left is None
    assert r.right is None


def test_removeLeafNodes_4():
    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(1)
    a.left = b
    b.right = c

    s = Solution()
    r = s.removeLeafNodes(a, 1)
    assert r is None


def test_removeLeafNodes_5():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c

    s = Solution()
    r = s.removeLeafNodes(a, 1)
    assert r.val == 1
    assert r.left.val == 2
    assert r.right.val == 3
