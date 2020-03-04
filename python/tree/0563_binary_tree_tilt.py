# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.whole_tilt = 0
        self.traverse(root)
        return self.whole_tilt

    def traverse(self, node):
        if node:
            tilt = abs(self.sum_tree(node.left) - self.sum_tree(node.right))
            self.whole_tilt += tilt
            self.traverse(node.left)
            self.traverse(node.right)

    def sum_tree(self, node):
        if not node:
            return 0
        return node.val + self.sum_tree(node.left) + self.sum_tree(node.right)


def test_find_tilt():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c

    s = Solution()
    assert 1 == s.findTilt(a)
