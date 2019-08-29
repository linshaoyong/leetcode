# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = [0]
        self.traversal(root, False, values)
        return values[0]

    def traversal(self, node, is_left, values):
        if node:
            if is_left and node.left is None and node.right is None:
                values[0] = values[0] + node.val
            self.traversal(node.left, True, values)
            self.traversal(node.right, False, values)


def test_sum_of_left_leaves():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    assert 24 == Solution().sumOfLeftLeaves(a)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    assert 4 == Solution().sumOfLeftLeaves(a)
