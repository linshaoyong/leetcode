# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def exchange(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.exchange(node.left)
            self.exchange(node.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.exchange(root)
        return root


def test_invert_tree():
    root = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(7)

    root.left = n1
    root.right = n2

    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n1.left = n3
    n1.right = n4

    n5 = TreeNode(6)
    n6 = TreeNode(9)
    n2.left = n5
    n2.right = n6

    s = Solution()
    s.invertTree(root)

    assert n2 == root.left
    assert n1 == root.right
    assert n6 == n2.left
    assert n5 == n2.right
    assert n4 == n1.left
    assert n3 == n1.right
