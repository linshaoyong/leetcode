# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        self.traverse(root, nodes)
        return self.sortedArrayToBST(nodes, 0, len(nodes) - 1)

    def traverse(self, node, nodes):
        if node:
            self.traverse(node.left, nodes)
            nodes.append(node)
            self.traverse(node.right, nodes)

    def sortedArrayToBST(self, nodes, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        parent = nodes[mid]
        parent.left = self.sortedArrayToBST(nodes, left, mid - 1)
        parent.right = self.sortedArrayToBST(nodes, mid + 1, right)
        return parent


def test_balance_bst_1():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.right = b
    b.right = c
    c.right = d

    s = Solution()
    root = s.balanceBST(a)
    assert 2 == root.val
    assert 1 == root.left.val
    assert root.left.left is None
    assert root.left.right is None
    assert 3 == root.right.val
    assert root.right.left is None
    assert 4 == root.right.right.val
    assert root.right.right.left is None
    assert root.right.right.right is None


def test_balance_bst_2():
    a = TreeNode(14)
    b = TreeNode(9)
    c = TreeNode(16)
    d = TreeNode(2)
    e = TreeNode(13)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    s = Solution()
    root = s.balanceBST(a)
    assert 13 == root.val
    assert 2 == root.left.val
    assert 9 == root.left.right.val
    assert 14 == root.right.val
    assert root.right.left is None
    assert 16 == root.right.right.val
