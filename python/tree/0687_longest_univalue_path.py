# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def traverse(node, parent_val):
            if not node:
                return 0
            left, right = traverse(node.left, node.val), traverse(
                node.right, node.val)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right) if node.val == parent_val else 0
        traverse(root, None)
        return self.longest


def test_longest_univalue_path():
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    assert 2 == Solution().longestUnivaluePath(a)

    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(4)
    e = TreeNode(4)
    f = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    assert 2 == Solution().longestUnivaluePath(a)

    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(1)
    g = TreeNode(1)
    a.right = b
    b.left = c
    b.right = d
    c.left = e
    c.right = f
    e.left = g
    assert 4 == Solution().longestUnivaluePath(a)
