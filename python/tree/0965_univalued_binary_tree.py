# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        value = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != value:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True


def test_is_unival_tree():
    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    assert Solution().isUnivalTree(a)

    a = TreeNode(2)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(5)
    e = TreeNode(2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    assert Solution().isUnivalTree(a) is False
