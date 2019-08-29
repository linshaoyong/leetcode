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
